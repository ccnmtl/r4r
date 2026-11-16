import React from 'react';
import Dashboard from './dashboard';
import TabList from './tabList';
import { generateNestedRoute } from './utils';


const faculty = <section>
    TODO - BUILD OUT FACULTY
</section>;

const interns = <section>
    TODO - BUILD OUT INTERNS
</section>;

const teams = <section>
    TODO - BUILD OUT TEAMS
</section>;

const membersTabs = [
    {path: 'teams', el: teams},
    {path: 'interns', el: interns},
    {path: 'faculty', el: faculty}
];

export const membersRoutes = generateNestedRoute(
    {path: 'members', el: <Members />},
    membersTabs
);

export default function Members() {
    return <Dashboard
        detail='Teams, interns and faculty in your rotations.'
        title='Members'
    >
        <TabList tabs={membersTabs} />
    </Dashboard>;
};