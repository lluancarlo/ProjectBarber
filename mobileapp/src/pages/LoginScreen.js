import React from 'react';
import styled from 'styled-components/native';
import { LoginButton, AccessToken } from 'react-native-fbsdk';

const imgBackground = require('../img/CorteCabelo.jpg');
const Page = styled.SafeAreaView`
  background-color: rgba(0,0,0,0.8);
  width: 200px;
  height: 100px;
  border: 2px solid;
  border-radius: 10px;
  justify-content: flex-start;
  align-items: center;
`;

const Title = styled.Text`
  color: #FFFFFF;
  font-size: 25px;
  padding-bottom: 25px;
`;

const ImageBkgr = styled.ImageBackground`
  flex: 1;
  resize-mode: cover;
  justify-content: center;
  align-items: center;
`;

export default (props) => {
  // Funcoes
  function getUserName(token) {
    fetch('https://graph.facebook.com/me?fields=id,name&access_token=' + token)
      .then((response) => response.json())
      .then((json) => {
        console.log(json.name);
      })
      .catch((error) => {
        console.error(error);
      });
  };

  return (
    <ImageBkgr source={imgBackground}>
      <Page>
        <Title>Entrar</Title>
        <LoginButton style={{width: 150, height: 30}}
          onLoginFinished={
              (error, result) => {
                  if (error) {
                      console.log("login has error: " + result.error);
                  } else if (result.isCancelled) {
                      console.log("login is cancelled.");
                  } else {
                      AccessToken.getCurrentAccessToken().then(
                          (data) => {
                              getUserName(data.accessToken.toString());
                              props.navigation.navigate('TabStack')
                          })
                  }
              }
          }
          onLogoutFinished={() => {
              console.log("logout.");
          }
        }/>
      </Page>
    </ImageBkgr>
  );
};