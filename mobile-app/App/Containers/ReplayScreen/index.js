// @flow

import React from 'react'

import {connect} from 'react-redux'
import {ScrollView, Text, Image, View, Dimensions, StyleSheet} from 'react-native'
import {Images} from '../../Themes'
import RoundedButton from '../../Components/RoundedButton'
import {Actions as NavigationActions} from 'react-native-router-flux'
import Pusher from 'pusher-js/react-native';
// Styles
import styles from '../Styles/PresentationScreenStyle'
import KeepAwake from 'react-native-keep-awake';
import Video from 'react-native-video'

const styles2 = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: 'black',
    paddingTop: 20,
    marginTop: 25,
  },
  fullScreen: {
    position: 'absolute',
    top: 0,
    left: 0,
    bottom: 0,
    right: 0,
    //width: 1200
  }
})

class ReplayScreen extends React.Component {


  componentDidMount() {
    this.player.seek(0)
  }

  render() {
    const imgStyle = {flex: 1, resizeMode: 'cover', width: null, height: null};
    return (
      <View style={styles.mainContainer}>
        <Image source={Images.background} style={imgStyle} resizeMode='stretch'>
        <Video
          source={{uri: "http://192.168.178.75/goal_replay.mp4"}}
                     ref={(ref) => {
               this.player = ref
             }}                             // Store reference
               rate={0.5}                     // 0 is paused, 1 is normal.
               volume={1.0}                   // 0 is muted, 1 is normal.
               muted={false}                  // Mutes the audio entirely.
               paused={false}                 // Pauses playback entirely.
               resizeMode="contain"             // Fill the whole screen at aspect ratio.
               style={styles2.fullScreen}
               onEnd={() => NavigationActions.pop()}
        />
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
  }
}

export default connect(mapStateToProps, mapDispatchToProps)(ReplayScreen)
