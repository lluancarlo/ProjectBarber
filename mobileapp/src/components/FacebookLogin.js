import React from 'react';
import { LoginButton, AccessToken } from 'react-native-fbsdk';

export default () => {
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
  // Retorno
  return (
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
                        })
                }
            }
        }
        onLogoutFinished={() => {
            console.log("logout.");
        }}/>
  );
}