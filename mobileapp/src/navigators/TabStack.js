import React from 'react';
import { Image } from 'react-native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
//
import ProfileScreen from '../pages/ProfileScreen';
import ScheduleScreen from '../pages/ScheduleScreen';
import PlaceScreen from '../pages/PlaceScreen';
//

const TabStack = createBottomTabNavigator();

export default () => {
    return (
        <TabStack.Navigator screenOptions={({route})=>({
            tabBarIcon: ({focused, color, size}) => {
                let imgSource = null;
                // para saber o nome da rota use ROUTE
                switch(route.name){
                    case 'Meu Perfil':
                        imgSource = require('../img/ProfileIcon.png')
                        break;
                    case 'Minha Agenda':
                        imgSource = require('../img/ScheduleIcon.png')
                        break;
                    case 'Locais':
                        imgSource = require('../img/LocationIcon.png')
                        break;
                }
            return <Image source={imgSource} style={{width: 30, height: 30}}/>
            }
        })}
        tabBarOptions={{
            activeBackgroundColor: '#ADD8E6',
            labelStyle: { 
                color: '#000000'
            } 
        }} 
        laze={true}>

            <TabStack.Screen name='Meu Perfil' component={ProfileScreen} />
            <TabStack.Screen name="Minha Agenda" component={ScheduleScreen} />
            <TabStack.Screen name="Locais" component={PlaceScreen} />

        </TabStack.Navigator>
    );
}