import * as React from 'react';

import PostModule from '../../modules/post';

export default class App extends React.Component {
    render (): React.ReactElement<'div'> {
        return (
            <div>
                <h1>Posts:</h1>
                <PostModule />
            </div>
        );
    }
}
