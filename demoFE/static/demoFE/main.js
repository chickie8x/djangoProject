$(document).ready(function () {
    //init chosen items
    var itemsList = {}

    // display diaglog items state
    var expandState = false


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
            if (link != 'void(0);'){
                var item = `<li><span>${title}</span><span class="btn-close">&times;</span></li>`
                $('#listqq').append(item)
                itemsList[link]=title
            }

        } else {
            console.log('unchecked')
        }
        $('#counter').text(Object.keys(itemsList).length.toString())
    })

    // show/hide chosen items list
    $('#toggle-show').click(function (){
        if(!expandState){
            $('#items-list').css('max-height', '400px')
            $('#items-list').css('overflow', 'auto')
        }
        else {
            $('#items-list').css('max-height', '0')
            $('#items-list').css('overflow', 'hidden')
        }
        expandState = !expandState
    })
})