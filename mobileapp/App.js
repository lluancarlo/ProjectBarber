import React from 'react';
import { SafeAreaView, Text, StyleSheet } from 'react-native';
import styled from 'styled-components/native';

const Texto = styled.Text`
  color: #FF0000;
  font-size: 30px;
`;

function TextoInicial(){
  return (
    <SafeAreaView>
      <Text>Ola mundo</Text>
    </SafeAreaView>
  );
}

export default (TextoInicial);