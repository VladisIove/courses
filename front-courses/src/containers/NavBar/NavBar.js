import React, {Component} from 'react'
import {MenuToggle} from './MenuToggle/MenuToggle'

export class NavBar extends Component{
    state = {
        menu:false,
    }
    toggleMenuHandler = () => {
        this.setState({
            menu: !this.state.menu
        })
    }
    render(){
        return (
            <React.Fragment>
                <MenuToggle onToggle={this.toggleMenuHandler} isOpen={this.state.menu}
                />
            </React.Fragment>
        )
    }

}