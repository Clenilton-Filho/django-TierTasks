
// Avança por um slot com loop
document.querySelectorAll('.toggle-btn').forEach(function(btn){

  // Evita dupla inicialização do mesmo botão
  if(btn.dataset.tierCarouselInit) return;
  btn.dataset.tierCarouselInit = '1';

  // Estado inicial (desabilita se total for menor ou igual a 3)
  (function(){

    // Encontra a section mais próxima para associar o botão à prioridade
    var sect = btn.closest('section');

    // Procura dentro da seção o elemento que contém as tarefas
    var t = sect && sect.querySelector('.carousel-track');

    // data-total é um atributo usado no HTML para informar quantas tarefas existem nesse grupo
    var total = t ? parseInt(t.getAttribute('data-total')) : 0;

    // Desabilita se o total for menor ou igual ao número de itens visíveis
    if(total <= 3){
      btn.disabled = true;
    }
  })();

  btn.addEventListener('click', function(){
    // Reacessa a section e track no clique
    var section = btn.closest('section')
    var track = section.querySelector('.carousel-track');

    // Quantidade de tarefas totais no grupo, vindo do data-total no template
    var total = parseInt(track.getAttribute('data-total'));

    // data-visible guarda o índice de quantas posições já foram avançadas
    var index = parseInt(track.getAttribute('data-visible'));

    // Índice máximo possível antes de voltar ao começo usamos total
    var maxIndex = Math.max(0, total - 3);

    // Incrementa enquanto não atingir maxIndex ou volta para 0
    index = (index < maxIndex) ? (index + 1) : 0;

    // Usa o width da primeira tarefa para saber quanto deslocar por vez
    var itemWidth = track.querySelector('.carousel-item').getBoundingClientRect().width;

    // Distância que precisa mover o track
    var shift = index * itemWidth;

    // Transform: translateX para mover o container
    track.style.transform = 'translateX(' + (-shift) + 'px)';

    // Atualizando o index
    track.setAttribute('data-visible', index);
  });
});
