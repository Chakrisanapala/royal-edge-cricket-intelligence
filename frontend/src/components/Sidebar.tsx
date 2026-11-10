import React from 'react';
import { NavLink } from 'react-router-dom';
import { 
  LayoutDashboard, 
  Activity, 
  ShieldAlert, 
  Target, 
  GitCompare, 
  Gavel, 
  UserCheck, 
  BookOpen,
  Crown
} from 'lucide-react';

interface SidebarProps {
  collapsed?: boolean;
  onToggle?: () => void;
}

export const Sidebar: React.FC<SidebarProps> = () => {
  const navItems = [
    { to: '/', label: 'Executive Overview', icon: LayoutDashboard },
    { to: '/pressure', label: 'Pressure Intelligence', icon: Activity },
    { to: '/batting', label: 'Batting Analytics', icon: Target },
    { to: '/bowling', label: 'Bowling Analytics', icon: ShieldAlert },
    { to: '/compare', label: 'Player Comparison', icon: GitCompare },
    { to: '/auction', label: 'Auction War Room', icon: Gavel },
    { to: '/profiles', label: 'Player Profiles', icon: UserCheck },
    { to: '/methodology', label: 'Methodology & Reliability', icon: BookOpen },
  ];

  return (
    <aside className="fixed top-0 left-0 h-screen w-64 bg-[#0D1C2D] border-r border-white/10 flex flex-col z-40 select-none">
      {/* Brand Header */}
      <div className="p-5 border-b border-white/10 flex items-center gap-3">
        <div className="w-10 h-10 rounded-lg bg-gradient-to-br from-[#EB107E] to-[#FABC4D] flex items-center justify-center p-0.5 shadow-lg shadow-[#EB107E]/20">
          <div className="w-full h-full bg-[#0D1C2D] rounded-[7px] flex items-center justify-center">
            <Crown className="w-5 h-5 text-[#FABC4D]" />
          </div>
        </div>
        <div>
          <div className="flex items-center gap-1.5">
            <span className="font-extrabold tracking-wider text-white text-base">ROYAL</span>
            <span className="font-extrabold tracking-wider text-[#EB107E] text-base">EDGE</span>
          </div>
          <p className="text-[10px] text-gray-400 font-medium tracking-tight">Rajasthan Royals · IPL 2027</p>
        </div>
      </div>

      {/* Navigation Links */}
      <nav className="flex-1 p-3 space-y-1 overflow-y-auto">
        <div className="px-3 py-2 text-[10px] font-bold uppercase tracking-wider text-gray-400">
          Intelligence Suite
        </div>
        {navItems.map((item) => {
          const Icon = item.icon;
          return (
            <NavLink
              key={item.to}
              to={item.to}
              className={({ isActive }) =>
                `flex items-center gap-3 px-3.5 py-2.5 rounded-lg text-xs font-semibold transition-all ${
                  isActive
                    ? 'bg-[#1C2B3C] text-[#EB107E] border-l-4 border-[#EB107E] shadow-sm'
                    : 'text-gray-300 hover:bg-[#122131] hover:text-white'
                }`
              }
            >
              <Icon className="w-4 h-4 shrink-0" />
              <span>{item.label}</span>
            </NavLink>
          );
        })}
      </nav>

      {/* Footer Info / Badge */}
      <div className="p-4 border-t border-white/10 bg-[#081320]">
        <div className="bg-[#122131] p-2.5 rounded-lg border border-white/5 flex items-center justify-between">
          <div>
            <div className="text-[10px] text-gray-400 uppercase font-semibold">Purse Capacity</div>
            <div className="text-xs font-bold text-[#FABC4D]">₹42.80 Cr Avail</div>
          </div>
          <span className="text-[10px] px-2 py-0.5 rounded bg-[#EB107E]/20 text-[#EB107E] font-medium">
            3 OS Slots
          </span>
        </div>
        <div className="mt-2 text-[10px] text-center text-gray-500">
          SupeRR Selector Season 2 Audited
        </div>
      </div>
    </aside>
  );
};

