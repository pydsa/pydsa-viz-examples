var graph_data;
    var barChartData;
    var data_iterator = 0;
    var color_r = Math.floor((Math.random() * 256));
    var color_g = Math.floor((Math.random() * 256));
    var opacity;
    $(document).ready(function(){
      $.ajax({
        async :false,
        url:"/sort/json",
        success:function(data){
          //console.log(data);
          graph_data=data;
          opacity=Math.max.apply(Math,data[0]);
          /*$.each(data,function(key,val){
            //console.log(val);
            graph_data=val;

          });*/

        }
      });
      //Add graph
      var barChartData = {
      labels : ['I','II','III','IV','V','VI','VII'],

        datasets : [
          {
            fillColor : ["rgba(220,220,220,0.5)","rgba(230,220,220,0.5)","rgba(220,220,220,0.5)","rgba(550,220,220,0.5)","rgba(220,220,220,0.5)","rgba(230,220,220,0.5)","rgba(220,220,220,0.5)"],
            strokeColor : "rgba(220,220,220,0.8)",
            highlightFill: "#3d4e3d",
            highlightStroke: "rgba(220,220,220,1)",
            data : graph_data[0]
          }
        ]

      }

      var ctx = document.getElementById("canvas").getContext("2d");
      window.myBar = new Chart(ctx).Bar(barChartData, {
        responsive : true
      });

      //End of graph

      var intr=setInterval(function() {
        if(data_iterator>=graph_data.length)
        {
          clearInterval(intr);
          return;
        }
        console.log(myBar.datasets[0].bars);
        //myBar.datasets[0].bars=graph_data[data_iterator];

        $("#output_print > code").prepend("Iteration " + (data_iterator+1) + ": <span>" + graph_data[data_iterator] + "</span><br>");
        $.each(myBar.datasets[0].bars,function(key,val) {
          cval = graph_data[data_iterator][0];
          cval2 = graph_data[data_iterator][key];
          myBar.datasets[0].bars[key].value = graph_data[data_iterator][key];
          myBar.datasets[0].bars[key].fillColor = "rgba(" + color_r + "," + color_g + "," + cval2+"," + cval2 + 2/opacity + ")";
          document.body.style.backgroundColor = "rgba(" + color_r + "," + color_g + "," + cval + "," + cval/opacity + ")";
        })
        myBar.update();
        data_iterator++;
      },1000);

  });
