import React, { useState } from 'react';
import { Text } from 'react-native';
import { LoginButton, AccessToken } from 'react-native-fbsdk';
import styled from 'styled-components/native';

const Page = styled.SafeAreaView`
  color: blue;
  flex: 1;
  justify-content: center;
  align-items: center;
`;

function TextoInicial(){
  // Constante
  const [ userName, setUserName ] = useState('');
  const [ mostrarNome, setMostrarNome ] = useState(false);
  // Funcoes
  function getUserName(token) {
    fetch('https://graph.facebook.com/me?fields=id,name&access_token=' + token)
      .then((response) => response.json())
      .then((json) => {
        setUserName(json.name);
        setMostrarNome(true);
      })
      .catch((error) => {
        console.error(error);
      });
  };
  // Retorno
  return (
    <Page>
      {mostrarNome &&
        <Text style={{color:'#FF0000', fontSize:25}}>Bem vindo {userName}!</Text>
      }
      <LoginButton
          onLoginFinished={
            (error, result) => {
              setMostrarNome(false);
              if (error) {
                console.log("login has error: " + result.error);
              } else if (result.isCancelled) {
                console.log("login is cancelled.");
              } else {
                AccessToken.getCurrentAccessToken().then(
                  (data) => {
                    getUserName(data.accessToken.toString());
                  }
                )
              }
            }
          }
          onLogoutFinished={() => {
            console.log("logout.");
            setMostrarNome(false);
          }}/>
    </Page>
  );
}

export default (TextoInicial);