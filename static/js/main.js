// Funções globais

// Remove alertas automaticamente após 5 segundos
document.querySelectorAll('[role="alert"]').forEach(function(alert){
  setTimeout(function(){
    if (alert && alert.remove) {
      alert.remove();
    } else if (alert && alert.parentElement) {
      alert.parentElement.removeChild(alert);
    }
  }, 5000);
});

// Confirmação de exclusão para forms com .confirm-delete (botão de excluir tarefa)
document.querySelectorAll('form.confirm-delete').forEach(function(f){
  f.addEventListener('submit', function(e){
    var msg = 'Tem certeza que deseja excluir esta tarefa?';
    if (!confirm(msg)) e.preventDefault();
  });
});
