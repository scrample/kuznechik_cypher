var tl = gsap.timeline({repeat: -1}),
  rightHandDown = '#right-hand-down',
  rightHandUp= '#right-hand-up',
  leftHandDown = '#left-hand-down',
  leftHandUp = '#left-hand-up',
  duration = 0.08

tl.fromTo(rightHandDown,{opacity: 100} , {
opacity: 0,
duration:duration
})
tl.fromTo(rightHandUp, {opacity: 0}, {
opacity: 100,
duration: duration
})
tl.addLabel('right-hand')

tl.to(leftHandDown, {
opacity: 0,
duration:duration
},"right-hand+=0.08")

tl.fromTo(leftHandUp, {opacity: 0}, {
opacity: 100,
duration: duration
})

$(function(){
  $('form').on('submit', function(e){
      var $template = $($("#bongo-cat").html());
      $('body').append($template)
  });
})