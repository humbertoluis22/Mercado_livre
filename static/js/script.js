
// precisa adicionar evento para fechar modal
function abrirModal(){
    let  modal = document.getElementById('janela-modal')
    modal.classList.add('abrir')
    modal.addEventListener('click',(e) =>{
        if(e.target.id =='fechar' || e.target.id == 'janela-modal')
            modal.classList.remove('abrir')
    })
    
}
