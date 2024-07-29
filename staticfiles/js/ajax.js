$(document).ready(function () {
    // Attach click event to pagination links
    $('.pagination a').on('click', function (e) {
        e.preventDefault();  // Prevent the default behavior of the link

        const url = $(this).attr('href');  // Get the URL from the clicked link

        // Perform an AJAX request
        $.ajax({
            url: url,
            type: 'GET',
            dataType: 'json',  // Expect JSON response
            success: function (data) {
                // Update the content container with the received HTML
                $('#your-service-container').html(data.html);
            },
            error: function (error) {
                console.log(error);
            }
        });
    });
});
