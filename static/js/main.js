// Funções globais, como fechar alertas
(function(){
  document.addEventListener('DOMContentLoaded', function(){

    // Fechar alertas usando elementos com .close-alert
    document.querySelectorAll('.close-alert').forEach(function(btn){
      if (btn.dataset.tierCloseInit) return;
      btn.dataset.tierCloseInit = '1';
      btn.addEventListener('click', function(){
        var parent = btn.parentElement;
        if (parent) parent.remove();
      });
    });

    // Confirmação de exclusão para forms com .confirm-delete
    document.querySelectorAll('form.confirm-delete').forEach(function(f){
      if (f.dataset.tierConfirmInit) return;
      f.dataset.tierConfirmInit = '1';
      f.addEventListener('submit', function(e){
        var msg = f.dataset.confirmMessage || 'Tem certeza que deseja excluir esta tarefa?';
        if (!confirm(msg)){
          e.preventDefault();
        }
      });
    });
  });
})();
