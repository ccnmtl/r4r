import React from 'react';
import { Outlet } from 'react-router-dom';
import Sidebar from './sidebar';
import Topbar from './topbar';
import Footer from './footer';
import { authUser } from './utils';

export default function Nav() {
    const staff = authUser.is_staff;

    return <div className={`d-flex${staff ? '' : ' flex-column'} vh-100`}>
        {staff ?
            <Sidebar unread={0} /> :
            <Topbar />}
        <main id="content" className="d-flex flex-column m-0 w-100 h-100">
            <div className="mb-auto p-4">
                <Outlet />
            </div>
            <Footer />
        </main>
    </div>;
}