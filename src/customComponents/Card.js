/**
 * Created by mephisto on 6/29/17.
 */
import React from 'react'

function Card(props) {
    return(
        <div className="col-sm-2 card">
            <img src={'/cards/'+props.card+'.png'} />
        </div>
    )
}

export default Card;