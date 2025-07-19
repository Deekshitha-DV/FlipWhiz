// This is the complete, correct, and final content for books/static/books/js/main.js
$(document).ready(function() {
    var flipbook = $('.flipbook');
    if (flipbook.length > 0) {
        function addPage(htmlContent, book) {
            var page = $('<div />').html(htmlContent);
            book.turn('addPage', page);
        }
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
        addPage('<div class="page back-cover"><h2>The End</h2></div>', flipbook);
        flipbook.turn({
            width: 800,
            height: 600,
            elevation: 50,
            gradients: true,
            autoCenter: true,
            duration: 1200,
            when: {
                turned: function(event, page, view) { $(this).find('a').css('pointer-events', 'auto'); },
                turning: function(event, page, view) { $(this).find('a').css('pointer-events', 'none'); }
            }
        });
    }
    var listenButton = $('#listen-button');
    var audioPlayer = $('#audio-player');
    if (listenButton.length > 0) {
        listenButton.on('click', function() {
            var streamUrl = window.location.pathname + 'listen/';
            audioPlayer.attr('src', streamUrl);
            audioPlayer.show();
            audioPlayer[0].play();
            $(this).text('Playing... Press Pause on Player to Stop');
            $(this).prop('disabled', true);
        });
    }
    var feedbackForm = $('#feedback-form');
    if (feedbackForm.length > 0) {
        var logoutButton = $('#final-logout-button');
        var feedbackTextareas = feedbackForm.find('textarea');
        function checkFeedback() {
            var hasContent = false;
            feedbackTextareas.each(function() { if ($(this).val().trim() !== '') { hasContent = true; } });
            logoutButton.prop('disabled', !hasContent);
        }
        feedbackTextareas.on('keyup', checkFeedback);
    }
    var sessionDataElement = $('#session-data');
    if (sessionDataElement.length > 0 && flipbook.length > 0) {
        var justLoggedOut = JSON.parse(sessionDataElement.text()).just_logged_out;
        if (justLoggedOut) {
            flipbook.turn('page', 1);
            setTimeout(function() { flipbook.addClass('closed'); }, 1000);
        }
    }
});