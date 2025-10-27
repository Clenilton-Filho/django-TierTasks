// Alternar entre tarefas (carousel) e botões do header
(function(){
  document.addEventListener('DOMContentLoaded', function(){
    var btnAdd = document.getElementById('btnOpenAdd');
    if(btnAdd && !btnAdd.dataset.tierHomeInit){
      btnAdd.dataset.tierHomeInit = '1';
      btnAdd.addEventListener('click', function(){
          window.scrollTo({top:0, behavior:'smooth'});
      });
    }

    // Avançar por um slot com loop
    document.querySelectorAll('.toggle-btn').forEach(function(btn){
      if(btn.dataset.tierCarouselInit) return;
      btn.dataset.tierCarouselInit = '1';

      // Estado inicial (desabilita se total for menor ou igual a 3)
      (function(){
        var sect = btn.closest('section');
        var t = sect && sect.querySelector('.carousel-track');
        var total = t ? parseInt(t.getAttribute('data-total') || 0, 10) : 0;
        if(total <= 3){
          btn.disabled = true;
          btn.setAttribute('aria-disabled', 'true');
        }
      })();

      btn.addEventListener('click', function(){
        var section = btn.closest('section');
        if(!section) return;
        var track = section.querySelector('.carousel-track');
        if(!track) return;
        // Quantidade de tarefas totais no grupo
        var total = parseInt(track.getAttribute('data-total') || 0, 10);
        // Quantidade de tarefas visíveis por grupo
        var visible = 3;
        var index = parseInt(track.getAttribute('data-visible') || 0, 10);
        var maxIndex = Math.max(0, total - visible);
        // Se o total de tarefas no grupo for menor ou igual a 3, desabilita o botão
        if(total <= visible){ btn.disabled = true; return; }
        index = (index < maxIndex) ? (index + 1) : 0;
        var firstItem = track.querySelector('.carousel-item');
        if(!firstItem) return;
        var itemWidth = firstItem.getBoundingClientRect().width;
        var shift = index * itemWidth;
        track.style.transform = 'translateX(' + (-shift) + 'px)';
        track.setAttribute('data-visible', index);
      });
    });
  });
})();
