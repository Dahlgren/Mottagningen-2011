$(document).ready(function(){
  
  var dagar = $('#days > .day');
  var scheman = $('#schema > .schema_dag');

  dagar.click(function(){
    dagar.index($(this));
  });

  
  $('#schema').css('height',
    $('#schema').children().first().height()
  );
  
  $('#schema').css('overflow', 'hidden');
  
});
