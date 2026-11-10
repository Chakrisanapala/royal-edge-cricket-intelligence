import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { Layout } from './components/Layout';
import { ExecutiveOverview } from './pages/ExecutiveOverview';
import { PressureIntelligence } from './pages/PressureIntelligence';
import { BattingAnalytics } from './pages/BattingAnalytics';
import { BowlingAnalytics } from './pages/BowlingAnalytics';
import { PlayerComparison } from './pages/PlayerComparison';
import { AuctionWarRoom } from './pages/AuctionWarRoom';
import { PlayerProfiles } from './pages/PlayerProfiles';
import { Methodology } from './pages/Methodology';

export function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<ExecutiveOverview />} />
          <Route path="pressure" element={<PressureIntelligence />} />
          <Route path="batting" element={<BattingAnalytics />} />
          <Route path="bowling" element={<BowlingAnalytics />} />
          <Route path="compare" element={<PlayerComparison />} />
          <Route path="auction" element={<AuctionWarRoom />} />
          <Route path="profiles" element={<PlayerProfiles />} />
          <Route path="methodology" element={<Methodology />} />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
