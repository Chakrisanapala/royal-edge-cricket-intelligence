import React from 'react';
import { Outlet, useLocation } from 'react-router-dom';
import { Sidebar } from './Sidebar';
import { Header } from './Header';

export const Layout: React.FC = () => {
  const location = useLocation();

  const getPageMeta = () => {
    switch (location.pathname) {
      case '/':
        return { title: 'Executive Overview', subtitle: 'Rajasthan Royals Front Office · IPL 2027 Macro Intelligence' };
      case '/pressure':
        return { title: 'Pressure Intelligence', subtitle: 'Ball-by-Ball Leverage Engine & Innings Phase Dynamics' };
      case '/batting':
        return { title: 'Batting Pressure Reliability (BPRI)', subtitle: 'Audited Statistical Rankings & Empirical Bayesian Priors' };
      case '/bowling':
        return { title: 'Bowling Pressure Reliability (BOWPRI)', subtitle: 'Containment Reliability & BCCI Actionability Segregation' };
      case '/compare':
        return { title: 'Player Comparison Studio', subtitle: 'Head-to-Head 6-Axis Radar & 95% Confidence Overlap' };
      case '/auction':
        return { title: 'Auction War Room', subtitle: 'Simulated Budget Ceilings, Overseas Quota & Squad Feasibility' };
      case '/profiles':
        return { title: 'Player Intelligence Profiles', subtitle: 'Deep-Dive Scouting Dossiers & Performance Bounds' };
      case '/methodology':
        return { title: 'Methodology & Statistical Rigor', subtitle: 'Empirical Bayesian Formulas, SSSI Interpretation & Audit Proof' };
      default:
        return { title: 'Intelligence Platform', subtitle: 'Rajasthan Royals Analytics' };
    }
  };

  const { title, subtitle } = getPageMeta();

  return (
    <div className="min-h-screen bg-[#051424] text-[#D4E4FA] flex">
      {/* 260px Fixed Sidebar */}
      <Sidebar />

      {/* Main Content Area */}
      <div className="flex-1 ml-64 flex flex-col min-w-0">
        <Header title={title} subtitle={subtitle} />
        <main className="flex-1 mt-16 p-6 overflow-y-auto">
          <Outlet />
        </main>
      </div>
    </div>
  );
};

