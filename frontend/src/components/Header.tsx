import React from 'react';
import { Search, Bell, Shield, Wallet } from 'lucide-react';

interface HeaderProps {
  title?: string;
  subtitle?: string;
}

export const Header: React.FC<HeaderProps> = ({ 
  title = "Intelligence Dashboard", 
  subtitle = "Rajasthan Royals Strategic Front Office" 
}) => {
  return (
    <header className="fixed top-0 left-64 right-0 h-16 bg-[#0D1C2D]/90 backdrop-blur-md border-b border-white/10 z-30 px-6 flex items-center justify-between">
      {/* Title & Breadcrumbs */}
      <div>
        <h1 className="text-sm font-bold text-white tracking-wide flex items-center gap-2">
          {title}
        </h1>
        <p className="text-[11px] text-gray-400">{subtitle}</p>
      </div>

      {/* Right Controls */}
      <div className="flex items-center gap-4">
        {/* Search Input */}
        <div className="relative hidden md:block">
          <Search className="w-3.5 h-3.5 text-gray-400 absolute left-3 top-1/2 -translate-y-1/2" />
          <input
            type="text"
            placeholder="Search players, metrics, roles..."
            className="w-64 bg-[#122131] border border-white/10 rounded-lg pl-9 pr-8 py-1.5 text-xs text-white placeholder-gray-400 focus:outline-none focus:border-[#EB107E] transition-all"
          />
          <span className="absolute right-2.5 top-1/2 -translate-y-1/2 text-[10px] font-mono text-gray-400 bg-white/5 px-1 rounded border border-white/10">
            ⌘K
          </span>
        </div>

        {/* Purse Tracker Badge */}
        <div className="flex items-center gap-2 bg-[#122131] border border-white/10 px-3 py-1.5 rounded-lg">
          <Wallet className="w-3.5 h-3.5 text-[#FABC4D]" />
          <div className="text-left">
            <span className="text-[10px] text-gray-400 block leading-tight">Simulated Purse</span>
            <span className="text-xs font-bold text-[#FABC4D] leading-tight">₹42.80 Cr</span>
          </div>
        </div>

        {/* User / Analyst Profile */}
        <div className="flex items-center gap-2 pl-2 border-l border-white/10">
          <div className="w-8 h-8 rounded-full bg-gradient-to-tr from-[#EB107E] to-[#7BD0FF] p-[1.5px] flex items-center justify-center">
            <div className="w-full h-full bg-[#0D1C2D] rounded-full flex items-center justify-center">
              <Shield className="w-4 h-4 text-[#EB107E]" />
            </div>
          </div>
          <div className="hidden lg:block text-left">
            <div className="text-xs font-semibold text-white">Lead Strategist</div>
            <div className="text-[10px] text-gray-400">RR Auction War Room</div>
          </div>
        </div>
      </div>
    </header>
  );
};

