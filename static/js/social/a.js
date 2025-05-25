{/* <script> */}
    $(document).ready(function () {

        // Show input and save button on edit
        $('#edit-bio').click(function () {
            $('#bio-text').hide();
            $('#bio-input').show();
            $('#save-bio').show();
        });

        // Submit form via AJAX
        $('#bio-form').submit(function (e) {
            e.preventDefault();  // Prevent default form submission

            const updatedBio = $('#bio-input').val();

            $.ajax({
                url: "/social/update_bio/",
                type: "POST",
                data: {
                    'bio': updatedBio,
                    'csrfmiddlewaretoken': '{{ csrf_token }}'
                },
                success: function (response) {
                    if (response.status === 'success') {
                        $('#change-bio').text(updatedBio);
                        $('#bio-text').show();
                        $('#bio-input').hide();
                        $('#save-bio').hide();
                        alert("Bio updated successfully!");
                    } else {
                        alert("Failed to update bio.");
                    }
                },
                error: function () {
                    alert("Error occurred while saving bio.");
                }
            });
        });
    });

{/* </script> */}