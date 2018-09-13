import * as React from 'react';
import * as ReactDOM from 'react-dom'
import { Provider, connect } from 'react-redux';

import store from 'core/redux/store';
import { RootState } from 'core/redux/reducers';
import * as actions from 'core/redux/actions';


interface Props {
    posts: string[],
    requestPosts: () => any,
}


class _App extends React.Component<Props> {
    render () {
        return (
            <div>
                <a href="#" onClick={this.props.requestPosts}>Load</a><br/>
                {this.props.posts.map(
                    (el, index) => {
                        return (
                            <div key={index}>
                                {el}
                            </div>
                        );
                    }
                )}
            </div>
        );
    }
}


const App = connect(
    (state: RootState) => {
        return {
            posts: state.posts
        }
    }, {
        requestPosts: actions.requestPosts,
    }
)(_App);

ReactDOM.render(
    <Provider store={store}>
        <App />
    </Provider>,
    document.getElementById('root')
);
