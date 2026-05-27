from django.db.models.signals import post_save
from django.dispatch import receiver
from timelines.models import PostModel


def _get_model():
    """Lazy-load the SentenceTransformer to avoid importing at module level
    (which would slow down every Django startup for unrelated commands)."""
    from sentence_transformers import SentenceTransformer
    return SentenceTransformer('all-MiniLM-L6-v2')


@receiver(post_save, sender=PostModel)
def compute_post_embedding(sender, instance, created, **kwargs):
    """Auto-generate and store the embedding when a post is saved.
    Uses update() to avoid triggering the signal recursively."""
    if not instance.content:
        return

    # Only recompute if newly created OR content changed (no embedding yet)
    if created or instance.embedding is None:
        try:
            model = _get_model()
            embedding = model.encode(instance.content).tolist()
            PostModel.objects.filter(pk=instance.pk).update(embedding=embedding)
        except Exception as e:
            print(f"Warning: Failed to generate embedding for post {instance.pk}: {e}")
