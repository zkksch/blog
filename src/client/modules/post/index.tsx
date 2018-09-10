import { connect } from 'react-redux';
import * as React from 'react';

import { Post } from '../../core/models/post';
import { loadPosts } from '../../core/actions';
import { RootState } from '../../core/reducers';
import { safeFetch } from '../../core/requests';

interface Props {
    posts: Post[],
    loadPosts: (...posts: Post[]) => any
}

interface State {

}

class PostModule extends React.Component<Props, State> {
    constructor (props: Props) {
        super(props);
    }

    renderPost (post: Post, idx: number) {
        return (
            <div key={idx}>
                <h6>{post.title}</h6>
                <div>{post.content}</div>
            </div>
        );
    }

    render (): React.ReactElement<'div'> {
        return (
            <div>
                <a href="#" onClick={() => {
                    safeFetch('/post', {}).then(
                        response => response.json().then(
                            data => this.props.loadPosts(...data)
                        )
                    );
                }}>Refresh</a>
                {this.props.posts.map(this.renderPost)}
            </div>
        );
    }
}


export default connect(
    (state: RootState) => {
        return {
            posts: state.post.posts
        }
    },
    {
        loadPosts: loadPosts
    }
)(PostModule);
