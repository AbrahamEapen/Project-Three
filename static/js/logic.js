var slider = document.getElementById("myRange");
var output = document.getElementById("rangeValue");
output.innerHTML = slider.value; // Display the default slider value

    //Variable to store slider value for distance
    var userDistance = output.innerHTML;

// Update the current slider value (each time you drag the slider handle)
slider.oninput = function() {
    userDistance = output.innerHTML = this.value;
}


    

function result(d, i){
    console.log("test result function", d.Result)
    if ( Math.abs((Math.round(d.Range) - userDistance)) < 40 ) {
        (d.Result === 1);
        console.log(d.Result)
        return (d.Result === 1)
       
    }
    else{
    
        return (d.Result === 0)
    }}
    
    
    // Width and height
    var w = 800;
    var h = 400;
    
//    // Data ( GET Request )
//    var queryURL = $.get("/generate", function(data) {
//                        console.log($.parseJSON(data))
//    })


//this is where we pull in the data
    var queryURL = "/generate/" + "userDistance" //"https://raw.githubusercontent.com/AbrahamEapen/Code-Iris/Mike/json11111.json" //"/generate" //"https://raw.githubusercontent.com/AbrahamEapen/Code-Iris/master/Front-End%20Site/js/newDatas.json"
    // Pull in the data
    d3.json(queryURL, function(error, dataset){
          //  console.log(dataset)
            
   
   
   
   
   
   
   
   
   
   
          //  console.log(x)
    // Create SVG element
    var svg = d3.select("#fireballCanvas")
                .append("svg")
                .attr("width", w)
                .attr("height", h);

//                  d3.select('#fireballCanvas')
//                 //  .append('svg')
//                 //  .attr({
//                 //     width: 300,
//                 //     height: 300,
//                 //     border: '1px solid #ccc'
//                 //   });
//             append('svg:image')
// .attr({
//   'xlink:href': 'ryu.png',  // can also add svg file here
//   x: 20,
//   y: 20,
//   width: 225,
//   height: 225
// }).enter();




     // create the circle
    var circles = svg.selectAll("circle")
        .data(dataset)
        .text(function(d, i) {
            return d.Velocity;
        })
        .attr("class", "label")
        .enter()
        .append("circle");

    circles.attr("cx", 5)
           .attr("cy", function(d, i) {
               try {
                   return (50)
               } 
               catch (err) {
                   console.log("you have experienced an error, sir!")
               }
           })
            .attr("r",10)// function(d, i){
        //     if (d.Result === 1) {
        //         return 20;
        //     }
        //     else{
        //         return 8;
        //     }})


           //start the animation of the circle
           d3.select("#Start")
           .on("click", function() {
               d3.selectAll("circle")
           .transition()
           .attr("cx", function(d, i) {
            if (d.Result === 1) {

                return (d.Range);
            } else {
                return (d.Range);
            }
           })

            //Color of the fireballs
            .attr("fill", function(d, i){
             //   console.log(userDistance);
              //  console.log(Math.round(d.Range));
                if ( Math.abs((Math.round(d.Range) - userDistance)) < 40 ) {
                    (d.Result === 1);
                  //  console.log(d.Result)
                    return "red";
                }
                else{
                   // console.log(d.Result)
                    return "yellow"
                }})
            .attr("stroke", "orange")
            .attr("stroke-width", function(d) {
                 return d/2;
            })
            .attr("opacity", 0.75)
           
           .attr("cy", function(d, i) {
            if (d.Result === 1) {
                return (300 + d.Velocity);
            } else {
                return (50 + d.Angle);
            }
           })
           .attr("cy", 300)
           .delay(function(d, i) {
               return d.Range * 15
           })
           .duration(500)
           .transition()
           .attr("r", 30)
           .duration(300)
           .transition()
           .attr("r", 8)

        //        function(d, i) {
        //        return (d.Range*8)
        //    })
           .attrTween('width', function() {
            return d3.interpolateNumber(0, 250);



          });



          function postSender(data){
            $.post("/train", data, function(data, response){
                // console.log(response);
                console.log("SUCCESFULLY SENT")
            })
         }
        
         $.get("/generate/" + userDistance, function(dataset) {
            //console.log(dataset[0])
            var testingData = JSON.stringify(dataset);
            console.log(testingData)
        
            postSender(testingData)
        })


           var rect = svg.selectAll("rect")
           .data(dataset)
           .enter()
           .append("rect")
           .attr("x", (userDistance - 30))
           .attr("y", 310   )
           .attr("height", 10)
           .attr("width", 60)
          
          
          // result(dataset)


           


          // console.log(userDistance);
        });


           //path
           // Create an arc generator with configuration
var arcGenerator = d3.arc();

// Generate the path string
var pathData = arcGenerator({
  startAngle: 0,
  endAngle: 0.25 * Math.PI,
  innerRadius: 50,
  outerRadius: 100
});

// Create a path element and set its d attribute
d3.select('g')
	.append('path')
	.attr('d', pathData);
});

// // Create function to POST Request Data Points back to Server
// $(function () {

//      var $ = $('#');
//      var $ = $('#');
//      var $ = $('#');

//      function addOrder(order){

//      }

//      $('').on('click', function(){

//          var order = {
//              name: $name.val(),    
//              drink: $drink.val(),
//          };

//          $.ajax({
//              type: 'POST',
//              url: "{{url_for('test')}}",
//              data: order,
//              contentType : 'application/json;charset=UTF-8'
//              data: {'data':clicked}
//              success: function(newData) {
//                  addOrder(newOrder);
//              },
//              error: function() {
//                     alert('error saving order');
//              }
//          });
//      });
//  });
// d3.select("#Train")
//            .on("click", function() {
//                $.post("/train", (userDistance) 
             
//              )  })
 

           d3.select("#Train")
            .on("click", function() {


              d3.json("/replay", function(error, dataset){

                  d3.selectAll("circle")
                             .transition()
                             .attr("cy", 10)
                             .attr("cx", 50)
                             .duration(500)
                             .transition()
                            // .attr("cx", 10)
                             .attr("r", 10)
                             .attr("fill", "yellow")
                             .duration(500)
                             .delay(200)
                                       
                             .duration(500)
                            // .delay(1500)
                             
                             .attr("fill", "red")
                             .attr("r", 30)
                             .duration(500)
                           //  .transition()
                             
                             .duration(3000)
                             .transition()
                             .duration(500)
                            // .attr("r", 10)
                             
                             .duration(500)
                             .transition()
                             .duration(1000)
                             .attr("r", 10)
                             
                             //.attr("cx",  userDistance ) 

                             .attr("cx", function(d, i){
                              //   console.log(userDistance);
                               //  console.log(Math.round(d.Range));
                                 if ( Math.abs((Math.round(d.Range) - userDistance)) < 40 ) {
                                     (d.Result === 1);
                                   //  console.log(d.Result)
                                     return d.Range1;
                                 }
                                 else{
                                    // console.log(d.Result)
                                     return d.Range1
                                 }})
                                 .delay(function (d, i) {
                                     return d.Range1;
                                 })
                                 .delay(100)
                             .attr("cy", 300)
                             .duration(500)
                          //   .attr("r", 10)




              })




              })



// //start the animation of the circle
//            d3.select("#Train")
//            .on("click", function() {
          
//             d3.json()

//           d3.selectAll("circle")
//            .transition()
//            .attr("cy", 10)
//            .attr("cx", 50)
//            .duration(500)
//            .transition()
//           // .attr("cx", 10)
//            .attr("r", 10)
//            .attr("fill", "yellow")
//            .duration(500)
//            .delay(200)
                     
//            .duration(500)
//           // .delay(1500)
           
//            .attr("fill", "red")
//            .attr("r", 30)
//            .duration(500)
//          //  .transition()
           
//            .duration(3000)
//            .transition()
//            .duration(500)
//           // .attr("r", 10)
           
//            .duration(500)
//            .transition()
//            .duration(1000)
//            .attr("r", 10)
           
//            //.attr("cx",  userDistance ) 

//            .attr("cx", function(d, i){
//             //   console.log(userDistance);
//              //  console.log(Math.round(d.Range));
//                if ( Math.abs((Math.round(d.Range) - userDistance)) < 40 ) {
//                    (d.Result === 1);
//                  //  console.log(d.Result)
//                    return d.Range;
//                }
//                else{
//                   // console.log(d.Result)
//                    return userDistance
//                }})
//                .delay(function (d, i) {
//                    return d.Range;
//                })
//                .delay(100)
//            .attr("cy", 300)
//            .duration(500)
//         //   .attr("r", 10)
           
//            })
