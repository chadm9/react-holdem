/**
 * Created by mephisto on 6/29/17.
 */
import React from 'react'

function ThePot(props) {
    return(
        <div className="col-sm-4 col-sm-offset-4 the-pot">
            ${props.wager}
        </div>
    )
}

export default ThePot;