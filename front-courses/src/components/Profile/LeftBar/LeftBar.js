import React from 'react';


export default class LeftBar extends React.Component{

    render(){
        return (
            <ul>
            <li><a href="#"><i class="fas fa-qrcode"></i>Dashboard</a></li>
            <li><a href="#"><i class="fas fa-link"></i>Shortcuts</a></li>
            <li><a href="#"><i class="fas fa-stream"></i>Overview</a></li>
            <li><a href="#"><i class="fas fa-calendar-week"></i>Events</a></li>
          </ul>
        )
    }
}