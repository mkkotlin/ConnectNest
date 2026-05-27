"""
Management command: python manage.py backfill_embeddings

Generates and stores sentence embeddings for all existing posts
that currently have embedding=null. Run this once after deploying
the timelines.signals upgrade.
"""
from django.core.management.base import BaseCommand
from sentence_transformers import SentenceTransformer
from timelines.models import PostModel


class Command(BaseCommand):
    help = "Backfill sentence embeddings for posts that have none stored yet."

    def add_arguments(self, parser):
        parser.add_argument(
            '--batch-size', type=int, default=64,
            help='Number of posts to encode per batch (default: 64)'
        )

    def handle(self, *args, **options):
        batch_size = options['batch_size']
        qs = PostModel.objects.filter(
            embedding__isnull=True
        ).exclude(content='').exclude(content__isnull=True)

        total = qs.count()
        if total == 0:
            self.stdout.write(self.style.SUCCESS("All posts already have embeddings. Nothing to do."))
            return

        self.stdout.write(f"Loading model…")
        model = SentenceTransformer('all-MiniLM-L6-v2')
        self.stdout.write(f"Encoding {total} post(s) in batches of {batch_size}…")

        posts = list(qs)
        for i in range(0, len(posts), batch_size):
            batch = posts[i:i + batch_size]
            contents = [p.content for p in batch]
            embeddings = model.encode(contents, show_progress_bar=False)

            for post, emb in zip(batch, embeddings):
                PostModel.objects.filter(pk=post.pk).update(embedding=emb.tolist())

            done = min(i + batch_size, total)
            self.stdout.write(f"  {done}/{total} posts processed…")

        self.stdout.write(self.style.SUCCESS(f"Done! {total} post(s) embedded successfully."))
