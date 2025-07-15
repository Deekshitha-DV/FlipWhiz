// This is the complete, correct, and final content for books/static/books/js/main.js

$(document).ready(function() {

    // ===================================
    // ===== FLIPBOOK INITIALIZATION =====
    // ===================================
    var flipbook = $('.flipbook');

    // Only run this code if the flipbook element exists on the page
    if (flipbook.length > 0) {
        
        // Helper function to add pages
        function addPage(htmlContent, book) {
            var page = $('<div />').html(htmlContent);
            book.turn('addPage', page);
        }

        // Get book data from the template's script tag
        var bookDataElement = $('#book-data');
        if (bookDataElement.length > 0) {
            var books = JSON.parse(bookDataElement.text());

            books.forEach(function(book) {
                var pageHtml = `
                    <div class="page-content">
                        ${book.category ? `<div class="ribbon-wrapper"><div class="ribbon">${book.category.name}</div></div>` : ''}
                        <div class="book-card">
                            <a href="${book.detail_url}">
                                ${book.cover_image_url ? `<img src="${book.cover_image_url}" alt="${book.title} Cover">` : ''}
                                <h3>${book.title}</h3>
                            </a>
                            <p>by ${book.author}</p>
                        </div>
                    </div>
                `;
                addPage(pageHtml, flipbook);
            });
        }

        // Add the back cover
        addPage('<div class="page back-cover"><h2>The End</h2></div>', flipbook);

        // Initialize the turn.js library
        flipbook.turn({
            width: 800,
            height: 600,
            elevation: 50,
            gradients: true,
            autoCenter: true,
            duration: 1200,
            when: {
                turned: function(event, page, view) {
                    $(this).find('a').css('pointer-events', 'auto');
                },
                turning: function(event, page, view) {
                    $(this).find('a').css('pointer-events', 'none');
                }
            }
        });

        // Click handler for dynamically added links in the flipbook
        $(document).on('click', '.flipbook a', function(event) {
            event.preventDefault();
            window.location.href = $(this).attr('href');
        });
    }


    // ===================================
    // ===== AUDIO PLAYER LOGIC =====
    // ===================================
    var listenButton = $('#listen-button');
    var audioPlayer = $('#audio-player');

    // Only run this code if the listen button exists on the page
    if (listenButton.length > 0) {
        
        listenButton.on('click', function() {
            // Build the URL for the audio stream, e.g., /library/book/1/listen/
            var streamUrl = window.location.pathname + 'listen/';
            
            // Set the audio player's source to our new stream URL
            audioPlayer.attr('src', streamUrl);
            
            // Show the audio player controls
            audioPlayer.show();
            
            // Tell the audio player to start playing
            audioPlayer[0].play();
            
            // Update the button to give the user feedback
            $(this).text('Playing... Press Pause on Player to Stop');
            $(this).prop('disabled', true); // Prevent multiple clicks
        });
    }

});