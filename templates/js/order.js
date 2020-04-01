
    //place sub order
    function addToCart(itemId,typeId){
        $("#hello").dialog()
        $.ajax({
            type: "POST",
            url: "/order/ordering",
            dataType: "json",
            data: {"item": itemId, "type": typeId, 'csrfmiddlewaretoken':window.CSRF_TOKEN},
        });
     
    };

    //place sub order
    function confirmOrder(){
        $.ajax({
            type: "POST",
            url: "/order/cartitem",
            dataType: "json",
            data: {"confirm": 1,  'csrfmiddlewaretoken':window.CSRF_TOKEN},
        });
     
    };

    //place sub order
    function confirmOrderItem(OrderId){
        $.ajax({
            type: "POST",
            url: "/order/orderlist",
            dataType: "json",
            data: {"confirm": 1, "OrderId": OrderId, 'csrfmiddlewaretoken':window.CSRF_TOKEN},
        });
        setTimeout(function(){
            window.location.reload();
         },100);
    };

    //place sub order
    function cancelOrder(OrderId){
        $.ajax({
            type: "POST",
            url: "/order/orderlist",
            dataType: "json",
            data: {"confirm": 0,  "OrderId" : OrderId,'csrfmiddlewaretoken':window.CSRF_TOKEN},
        });
        setTimeout(function(){
            window.location.reload();
         },100);
     
    };

    