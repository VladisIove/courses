import React from 'react';
import {connect} from 'react-redux';
import classes from './FAQ.module.scss';
import { GET_FAQ, setYear } from '../../redux-courses/FAQ/actions';



const FAQ = (props) =>{

    return  (
        <div className={classes.BG}>
            <div className={classes.FAQ}>
                <div className={classes.Header}>
                    <p className={classes.HeaderFAQ}>Тут собраны самые часто задаваемые вопросы</p>
                    <p className={classes.HeaderText}>Ullamco commodo nisi officia consequat incididunt incididunt officia. Consequat reprehenderit esse culpa elit consequat aliquip veniam in ullamco cupidatat ipsum proident. Id qui consequat magna qui velit ex consectetur Lorem.</p>
                </div>
                <div className={classes.FAQMain}>
                    {props.faqs.map(q => (
                        <div key={q.id} className={classes.QuestionPart}>
                            <p className={classes.Question}>{q.question}</p>
                            <p className={classes.Answer}>{q.answer}</p>
                        </div>
                    ))} 
                </div>
    
            </div>
        </div>
    )
}

const mapStateToProps = store => {
    return {
        faqs: store.reduserFAQ
    }
}
  
export default connect(mapStateToProps)(FAQ);