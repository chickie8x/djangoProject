$(document).ready(function () {

    // inject checkbox
    var h = $('h3,h2')
    h.each(function () {
        var inp = $("<input type='checkbox' class='hook-action'>")
        $(this).prepend(inp)
    })

    // onclick checkbox event
    $('.hook-action').change(function () {
        if ($(this).is(':checked')) {
            var title = $(this).next('a')[0].innerText
            var link = $(this).next('a')[0]['pathname']
            console.log(link === 'void(0);' ? 'invalid link' : link)
        } else {
            console.log('unchecked')
        }
    })

})