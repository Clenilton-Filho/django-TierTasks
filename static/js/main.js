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

    // Remove alertas automaticamente após 5 segundos
    document.querySelectorAll('[role="alert"]').forEach(function(alert){
      if(alert.dataset.tierAutoInit) return;
      alert.dataset.tierAutoInit = '1';
      try{
        setTimeout(function(){
          if(alert && alert.parentElement) alert.parentElement.removeChild(alert);
        }, 5000);
      }catch(e){  }
    });

    // Confirmação de exclusão para forms com .confirm-delete (botão de excluir tarefa)
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
