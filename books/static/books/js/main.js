// This is the complete and correct final content for books/static/books/js/main.js

$(document).ready(function() {
    var flipbook = $('.flipbook');

    // Function to add a page to the flipbook
    // This is a helper to make the code cleaner
    function addPage(htmlContent, book) {
        var page = $('<div />').html(htmlContent);
        book.turn('addPage', page);
    }

    // --- Let's build the book dynamically ---

    // 1. Get the book data from the script tag in the HTML
    var bookDataElement = $('#book-data');
    if (bookDataElement.length > 0) {
        var books = JSON.parse(bookDataElement.text());

        // 2. Loop through each book and create an HTML page for it
        books.forEach(function(book) {
            // Create the HTML string for a single book page
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
            // Add this new page to the flipbook
            addPage(pageHtml, flipbook);
        });
    }

    // 3. Add the static back cover after all book pages
    addPage('<div class="page back-cover"><h2>The End</h2></div>', flipbook);

    // 4. Now that all pages are added, initialize the turn.js library
    flipbook.turn({
        width: 800,
        height: 600,
        elevation: 50,
        gradients: true,
        autoCenter: true,
        duration: 1200,

        // This part handles making links clickable
        when: {
            turned: function(event, page, view) {
                // Re-enable links after a page turn is complete
                $(this).find('a').css('pointer-events', 'auto');
            },
            turning: function(event, page, view) {
                // Disable links while the page is turning
                $(this).find('a').css('pointer-events', 'none');
            }
        }
    });

    // A safeguard to make sure clicks work on dynamically added links
    $(document).on('click', '.flipbook a', function(event) {
        event.preventDefault();
        window.location.href = $(this).attr('href');
    });
});