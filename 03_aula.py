from time import sleep
import streamlit as st

from crud import le_todos_usuarios

def login():
    usuarios = le_todos_usuarios()
    usuarios= {usuario.nome: usuario for usuario in usuarios}
    with st.container(border=True):
        st.markdown('Bem-vindos ao AppFerias')
        nome_usuario = st.selectbox('Selecione o seu usuário', usuarios.keys())
        senha = st.text_input('Digite sua senha', type='password')
        if st.button('Acessar'):
            usuario = usuarios[nome_usuario]
            if usuario.verifica_senha(senha):
                st.success('Login efetuado com sucesso')
                st.session_state['logado'] = True
                st.session_state['usuario'] = usuario
                sleep(1)
                st.rerun()
            else:
                st.error('Senha incorreta')

def pagina_calendario():
    st.markdown('Página Calendário')

def main():
    if not 'logado' in st.session_state:
        st.session_state['logado'] = False
    
    if not st.session_state['logado']:
        login()
    else:
        pagina_calendario()


if __name__ == '__main__':
    main()