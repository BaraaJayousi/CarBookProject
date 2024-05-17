$(()=>{
  // handle cancel booking form submission
  $("#bookings_table").on('click',".cancel_booking_submit", (elem) =>{
    elem.preventDefault()
    form_data = $($(elem)[0].target.form).serialize()
    
    $.ajax({
        type: "POST",
        url: "/cars/my-bookings/cancel",
        data: form_data,
        success: function (response) {
          $("#bookings_table").html(response)
        }
      });
  })


  $("#filter-cars").submit((elem) => {
    elem.preventDefault()
    $.ajax({
      type: "POST",
      url: "/cars/",
      data:$("#filter-cars").serialize(),
      success: (response) => {
        $("#search_results").html(response)
      }
    })
  })
})