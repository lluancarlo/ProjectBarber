import React from 'react';
import { createStackNavigator } from '@react-navigation/stack';
//
import LoginScreen from '../pages/LoginScreen';
import TabStack from './TabStack';

const MainStack = createStackNavigator();

export default () => {
    return (
        <MainStack.Navigator>
            <MainStack.Screen name='LoginScreen' component={LoginScreen} options={{ headerShown: false }}/>
            <MainStack.Screen name='TabStack' component={TabStack} options={{ headerShown: false }}/>
        </MainStack.Navigator>
    );
}