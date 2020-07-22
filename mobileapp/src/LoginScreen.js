import React from 'react';
import styled from 'styled-components/native';
import FacebookLogin from './components/FacebookLogin'

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

export default () => {
  return (
    <ImageBkgr source={require('./img/CorteCabelo.jpg')}>
      <Page>
        <Title>Entrar</Title>
        <FacebookLogin />
      </Page>
    </ImageBkgr>
  );
};