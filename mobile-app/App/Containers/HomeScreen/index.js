// @flow

import React from 'react'

import {connect} from 'react-redux'
import {ScrollView, Text, Image, View, Dimensions} from 'react-native'
import {Images} from '../../Themes'
import RoundedButton from '../../Components/RoundedButton'
import {Actions as NavigationActions} from 'react-native-router-flux'
import {startGameRequest, goalScored, stopGame} from './actions';
import Pusher from 'pusher-js/react-native';
// Styles
import styles from '../Styles/PresentationScreenStyle'
import KeepAwake from 'react-native-keep-awake';
import {PUSHER_KEY} from '../../Config/config'

// connect to pusher channel
// Enable pusher logging - don't include this in production
//Pusher.logToConsole = true;

var pusher = new Pusher(PUSHER_KEY, {
  cluster: 'eu',
  encrypted: false
});



class HomeScreen extends React.Component {

  startGame() {
    const {goalScored} = this.props
    let channel = pusher.subscribe('kicker_channel');
    channel.bind('goal_scored', function(data) {
      goalScored(data.player)
    });
    this.props.startGame()
  }

  stopGame() {
    pusher.unsubscribe('kicker_channel');
    this.props.stopGame()
  }

  componentWillUnmount() {
    pusher.unsubscribe('kicker_channel');
  }

  render() {

    const imgStyle = {flex: 1, resizeMode: 'cover', width: null, height: null};

    const {status, score} = this.props.game;


    return (
      <View style={styles.mainContainer}>
        <Image source={Images.background} style={imgStyle} resizeMode='stretch'>
          <View style={{flex: 2}}>
            <KeepAwake />
            {!status ?
              null
              :
              <View style={{flex: 2}}>
                <View style={{flex: 1, flexDirection: 'row', justifyContent: 'center',}}>
                  <View style={{width:200}}><Text style={{fontSize: 150, textAlign: 'center'}}>{score[0]}</Text></View>
                  <View style={{width:20}}><Text style={{fontSize: 150, textAlign: 'center'}}>:</Text></View>
                  <View style={{width:200}}><Text style={{fontSize: 150, textAlign: 'center'}}>{score[1]}</Text></View>
                </View>
              </View> }
          </View>
          {status === 'running' || status === 'overtime' ?
            <View style={{flex: 1}}>
              <View style={{flex: 1, flexDirection: 'row', justifyContent: 'space-between',}}>
                <RoundedButton onPress={() => this.props.goalScored(0)}>Goal Player 1</RoundedButton>
                <RoundedButton onPress={() => this.stopGame()}>Abort Game</RoundedButton>
                <RoundedButton onPress={() => this.props.goalScored(1)}>Goal Player 2</RoundedButton>
              </View>
            </View> : null }
          {status === 'over' ?
            <View style={{flex: 1}}>
              <RoundedButton onPress={() => this.startGame()}>Start new Game</RoundedButton>
            </View> : null}
          {!status ?
            <View style={{flex: 1}}>
              <RoundedButton onPress={() => this.startGame()}>Start new Game</RoundedButton>
            </View> : null}
        </Image>
      </View>
    )
  }
}

const mapStateToProps = (state) => {
  return {
    game: state.game
  }
}

const mapDispatchToProps = (dispatch) => {
  return {
    startGame: () => dispatch(startGameRequest()),
    goalScored: (player) => dispatch(goalScored(player)),
    stopGame: () => dispatch(stopGame()),
  }
}

export default connect(mapStateToProps, mapDispatchToProps)(HomeScreen)
