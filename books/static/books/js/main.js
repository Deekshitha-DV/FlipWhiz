// Corrected main.js file

$(document).ready(function() {
    var flipbook = $('.flipbook');

    // Initialize the flipbook
    flipbook.turn({
        width: 800,
        height: 600,
        elevation: 50,
        gradients: true,
        autoCenter: true,  // <-- Comma is here
        duration: 1200,    // <-- And a comma here for good practice

        when: {
            turning: function(event, page, view) {
                // Find all links in the flipbook and disable them during the turn
                flipbook.find('a').css('pointer-events', 'none');
            },
            turned: function(event, page, view) {
                // Re-enable the links when the page turn is complete
                flipbook.find('a').css('pointer-events', 'auto');
            }
        }
    });

    // An extra safeguard for clicks
    flipbook.on('click', 'a', function(event) {
        // This makes sure the link click is prioritized
        window.location.href = $(this).attr('href');
    });
});