$(document).ready(function () {
    //csrf toke
    var csrf = $("input[name=csrfmiddlewaretoken]").val();

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
                var item = `<li data-key= ${link}><span>${title}</span><span class="btn-close">&times;</span></li>`
                $('#listqq').prepend(item)
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

    // remove item from list
    $('#listqq').on('click','.btn-close',function () {
        var itemKey =  $(this).parent().data("key")
        delete itemsList[itemKey]
        $(this).parent().remove()
        $('#counter').text(Object.keys(itemsList).length.toString())
        $('.hook-action').each(function () {
            if ($(this).next()[0]['pathname'] && $(this).next()[0]['pathname']===itemKey){
                $(this).prop('checked', false)
            }
        })
    })

    // button crawl event
    $('#btn-crawl').click(function () {
        items = []
        Object.keys(itemsList).map(item => {
            items.push(item)
        })
        $.ajax({
            url: '/crawl/',
            type: 'post',
            data: {
                csrfmiddlewaretoken: csrf,
                links: items.toString()
            },
            success: function (res){
                alert(res.mes)
            },
            error: function () {
                alert('problem occured when request to server!')
            }
        })
    })




})