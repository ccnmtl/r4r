import React from 'react';
import Dashboard from './dashboard';
import TabList from './tabList';
import { generateNestedRoute} from './utils';


const promptSequence = <section>
    TODO - BUILD OUT PROMPT SEQUENCE
</section>;

const quizzes = <section>
    TODO - BUILD OUT STATIC QUIZZES
</section>;


const rounds = <section>
    TODO - BUILD OUT ROUNDS
</section>;

const staticMedia = <section>
    TODO - BUILD OUT STATIC MEDIA
</section>;

const urls = <section>
    TODO - BUILD OUT URLS
</section>;

const rotationTabs = [
    {path: 'prompt-sequence', el: promptSequence},
    {path: 'static-media', el: staticMedia},
    {path: 'urls', el: urls},
    {path: 'rounds', el: rounds},
    {path: 'quizzes', el: quizzes}
];

export const rotationRoutes = generateNestedRoute(
    {path: 'rotation/:rotationId', el: <Rotation />},
    rotationTabs);

export default function Rotation() {
    return <Dashboard
        detail='Teams, interns and faculty in your rotations.'
        title='Rotation'
    >
        <TabList tabs={rotationTabs}/>
    </Dashboard>;
};