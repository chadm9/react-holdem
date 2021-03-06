/**
 * Created by mephisto on 6/29/17.
 */
import React, { Component } from 'react'

class Buttons extends Component{

    render() {



        return (
            <div className="col-sm-12 buttons">
                <div className="col-sm-4">
                    <button onClick={this.props.deal} className="btn btn-info">Deal</button>
                </div>
                <div className="col-sm-2">
                    <button onClick={()=>{this.props.bet(10)}} className="btn btn-info">Bet 10</button>
                </div>
                <div className="col-sm-2">
                    <button onClick={()=>{this.props.bet(100)}} className="btn btn-info">Bet 100</button>
                </div>
                <div className="col-sm-4">
                    <button className="btn btn-info">Check</button>
                </div>
            </div>
        )
    }
}

export default Buttons