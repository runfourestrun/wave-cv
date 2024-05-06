import React from 'react';
import { Header } from './components/Header';
import { SideBar } from './components/SideBar';
import { Results } from './components/Results';

function App() {
    return (
        <div className="App">
            <Header />
            <div className="flex">
                <SideBar />
                <Results />
            </div>
        </div>
    );
}

export default App;
