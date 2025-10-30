// Scripts para os modais com data-attributes
(function(){

  // Abrir o modal
  function openModal(sel){
    var el = document.querySelector(sel);
    if(!el) return;
    el.classList.remove('hidden');
    document.body.classList.add('overflow-y-hidden');
  }

  // Fechar o modal
  function closeModal(sel){
    var el = document.querySelector(sel);
    if(!el) return;
    el.classList.add('hidden');
    document.body.classList.remove('overflow-y-hidden');
  }

  // Adicionando os listeners para as funções anteriores ao carregar a página
  document.addEventListener('DOMContentLoaded', function(){

    // Abrir modal usando elementos com data-open-modal (Ex: ícone de informação)
    document.querySelectorAll('[data-open-modal]').forEach(function(btn){
      if(btn.dataset.tierOpenInit) return;
      btn.dataset.tierOpenInit = '1';
      btn.addEventListener('click', function(e){
        // Botões/forms que possam existir dentro do elemento que abre um modal
        var interactiveEl = e.target.closest('button,form');
        if(interactiveEl){

            // Se o botão/form também abre um modal, permite (ex: botão de modificar)
            var interactiveNearestOpener = interactiveEl.closest('[data-open-modal]');
            var interactiveIsOpener = interactiveEl.hasAttribute('data-open-modal') || (interactiveNearestOpener && interactiveNearestOpener !== btn);

            // Se o botão/form não abre um modal, ignorar para não abrir o modal em sequência (ex: botão de excluir)
            if(interactiveNearestOpener === btn && !interactiveIsOpener){
              return;
            }
          }
        var sel = btn.getAttribute('data-open-modal');
        if(!sel) return;
        openModal(sel, btn);
      });
    });

    // Fechar modal usando elementos com data-close-modal (Ex: botão X)
    document.querySelectorAll('[data-close-modal]').forEach(function(btn){
      if(btn.dataset.tierCloseInit) return;
      btn.dataset.tierCloseInit = '1';
      btn.addEventListener('click', function(){
        var sel = btn.getAttribute('data-close-modal');
        if(!sel) return;
        closeModal(sel);
      });
    });

    // Enviar form usando elementos com data-submit-form e fechar modal
    document.querySelectorAll('[data-submit-form]').forEach(function(btn){
      if(btn.dataset.tierSubmitInit) return;
      btn.dataset.tierSubmitInit = '1';
      btn.addEventListener('click', function(){
        var formSel = btn.getAttribute('data-submit-form');
        if(!formSel) return;
        var form = document.querySelector(formSel);
        try{
          if(form){
            if(typeof form.requestSubmit === 'function') form.requestSubmit();
            else form.submit();
          }
        }catch(e){
          try{ if(form) form.submit(); }catch(_){ }
        }
        var closeSel = btn.getAttribute('data-close-modal');
        if(closeSel) closeModal(closeSel);
      });
    });

    // Clicando para fora fecha os modais com .modal-backdrop
    document.querySelectorAll('.modal-backdrop').forEach(function(backdrop){
      if(backdrop.dataset.tierBackdropInit) return;
      backdrop.dataset.tierBackdropInit = '1';
      backdrop.addEventListener('click', function(e){
        if(e.target === backdrop){
          var sel = backdrop.id ? ('#' + backdrop.id) : null;
          if(sel) closeModal(sel);
          else backdrop.classList.add('hidden');
        }
      });
    });
  });
})();
