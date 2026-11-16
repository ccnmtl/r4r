import React from 'react';
import Dashboard from './dashboard';
import TabList from './tabList';
import { generateNestedRoute } from './utils';


const comments = <section>
    TODO - BUILD OUT COMMENTS
</section>;

const interns = <section>
    TODO - BUILD OUT INTERNS
</section>;

const rounds = <section>
    TODO - BUILD OUT ROUNDS
</section>;

const teams = <section>
    TODO - BUILD OUT TEAMS
</section>;

const feedbackTabs = [
    {path: 'comments', el: comments},
    {path: 'interns', el: interns},
    {path: 'rounds', el: rounds},
    {path: 'teams', el: teams}
];

export const feedbackRoutes = generateNestedRoute(
    {path: 'feedback', el: <Feedback />},
    feedbackTabs
);

export default function Feedback() {
    return <Dashboard
        detail={`Intern comments from rounds, grouped by team, round, and 
            intern.`}
        title='Feedback'
    >
        <TabList tabs={feedbackTabs} />
    </Dashboard>;
};