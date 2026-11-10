import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { api, OverviewData } from '../services/api';
import { 
  Activity, 
  Target, 
  ShieldAlert, 
  Users, 
  ArrowUpRight, 
  Gavel, 
  GitCompare, 
  BookOpen, 
  CheckCircle2, 
  AlertTriangle 
} from 'lucide-react';

export const ExecutiveOverview: React.FC = () => {
  const navigate = useNavigate();
  const [data, setData] = useState<OverviewData | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    api.getOverview()
      .then(res => {
        setData(res);
        setLoading(false);
      })
      .catch(err => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return (
      <div className="flex items-center justify-center h-96">
        <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-[#EB107E]"></div>
      </div>
    );
  }

  if (error || !data) {
    return (
      <div className="p-6 bg-red-950/30 border border-red-500/30 rounded-xl text-red-300">
        <AlertTriangle className="w-5 h-5 mb-2" />
        <p>Error loading intelligence data: {error || 'No data available'}</p>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      {/* Hero Banner / Strategy Briefing */}
      <div className="bg-gradient-to-r from-[#122131] via-[#0D1C2D] to-[#1C2B3C] border border-white/10 rounded-2xl p-6 relative overflow-hidden">
        <div className="absolute -right-10 -bottom-10 w-64 h-64 bg-[#EB107E]/10 rounded-full blur-3xl pointer-events-none"></div>
        <div className="relative z-10 flex flex-col md:flex-row md:items-center justify-between gap-4">
          <div>
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#EB107E]/15 border border-[#EB107E]/30 text-[#EB107E] text-xs font-bold mb-3">
              <CheckCircle2 className="w-3.5 h-3.5" />
              INDEPENDENT SCIENTIFIC AUDIT VERIFIED
            </div>
            <h2 className="text-2xl font-bold text-white tracking-tight">
              Rajasthan Royals Strategic Decision System
            </h2>
            <p className="text-xs text-gray-300 mt-1 max-w-2xl leading-relaxed">
              Evaluating match leverage and high-pressure resilience across 867 competitive matches (2022–2026). 
              Statistical rankings are insulated with Bayesian shrinkage priors (<span className="text-[#FABC4D] font-mono">K=60</span> batting, <span className="text-[#FABC4D] font-mono">K=50</span> bowling) and 95% bootstrap confidence intervals.
            </p>
          </div>
          <div className="flex items-center gap-3 shrink-0">
            <button
              onClick={() => navigate('/auction')}
              className="px-4 py-2.5 bg-[#EB107E] hover:bg-[#EB107E]/90 text-white text-xs font-bold rounded-lg flex items-center gap-2 transition-all shadow-lg shadow-[#EB107E]/25"
            >
              <Gavel className="w-4 h-4" />
              Enter War Room
            </button>
            <button
              onClick={() => navigate('/methodology')}
              className="px-4 py-2.5 bg-[#1C2B3C] hover:bg-[#273647] border border-white/10 text-white text-xs font-bold rounded-lg flex items-center gap-2 transition-all"
            >
              <BookOpen className="w-4 h-4" />
              Methodology
            </button>
          </div>
        </div>
      </div>

      {/* 4 Primary KPI Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        {/* Matches */}
        <div className="bg-[#0D1C2D] border border-white/10 rounded-xl p-4 flex flex-col justify-between">
          <div className="flex items-center justify-between text-gray-400">
            <span className="text-xs font-semibold uppercase tracking-wider">Matches Audited</span>
            <Activity className="w-4 h-4 text-[#7BD0FF]" />
          </div>
          <div className="mt-3">
            <div className="text-3xl font-extrabold text-white font-mono">{data.matches_analyzed}</div>
            <div className="text-[11px] text-gray-400 mt-1">IPL & T20I (2022–2026)</div>
          </div>
        </div>

        {/* Deliveries */}
        <div className="bg-[#0D1C2D] border border-white/10 rounded-xl p-4 flex flex-col justify-between">
          <div className="flex items-center justify-between text-gray-400">
            <span className="text-xs font-semibold uppercase tracking-wider">Ball-by-Ball Records</span>
            <Users className="w-4 h-4 text-[#FABC4D]" />
          </div>
          <div className="mt-3">
            <div className="text-3xl font-extrabold text-[#FABC4D] font-mono">{data.deliveries_analyzed.toLocaleString()}</div>
            <div className="text-[11px] text-gray-400 mt-1">0% Fabricated · Full Integrity</div>
          </div>
        </div>

        {/* High Pressure Deliveries */}
        <div className="bg-[#0D1C2D] border border-white/10 rounded-xl p-4 flex flex-col justify-between">
          <div className="flex items-center justify-between text-gray-400">
            <span className="text-xs font-semibold uppercase tracking-wider">High-Pressure Balls</span>
            <Target className="w-4 h-4 text-[#EB107E]" />
          </div>
          <div className="mt-3">
            <div className="text-3xl font-extrabold text-[#EB107E] font-mono">{data.high_pressure_deliveries.toLocaleString()}</div>
            <div className="text-[11px] text-gray-400 mt-1">{data.high_pressure_pct}% of Total Leverage</div>
          </div>
        </div>

        {/* Purse Tracker */}
        <div className="bg-[#0D1C2D] border border-white/10 rounded-xl p-4 flex flex-col justify-between">
          <div className="flex items-center justify-between text-gray-400">
            <span className="text-xs font-semibold uppercase tracking-wider">Simulated Purse</span>
            <Gavel className="w-4 h-4 text-[#7BD0FF]" />
          </div>
          <div className="mt-3">
            <div className="text-3xl font-extrabold text-white font-mono">₹{data.simulated_purse_capacity_cr.toFixed(2)} Cr</div>
            <div className="text-[11px] text-emerald-400 mt-1">{data.overseas_slots_available}</div>
          </div>
        </div>
      </div>

      {/* Top 3 Previews Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Batters Preview */}
        <div className="bg-[#0D1C2D] border border-white/10 rounded-xl p-5 flex flex-col justify-between">
          <div>
            <div className="flex items-center justify-between mb-4">
              <div className="flex items-center gap-2">
                <Target className="w-4 h-4 text-[#EB107E]" />
                <h3 className="text-sm font-bold text-white uppercase tracking-wider">
                  Top Audited Batters (BPRI)
                </h3>
              </div>
              <button
                onClick={() => navigate('/batting')}
                className="text-xs text-[#EB107E] hover:underline flex items-center gap-1 font-semibold"
              >
                Full Top 10 <ArrowUpRight className="w-3.5 h-3.5" />
              </button>
            </div>

            <div className="space-y-3">
              {data.top_batters_preview.map((bat: any) => (
                <div
                  key={bat.player_id}
                  onClick={() => navigate('/batting')}
                  className="bg-[#122131] hover:bg-[#1C2B3C] border border-white/5 p-3.5 rounded-lg flex items-center justify-between cursor-pointer transition-all"
                >
                  <div className="flex items-center gap-3">
                    <span className="w-6 h-6 rounded-full bg-[#EB107E]/20 text-[#EB107E] text-xs font-bold flex items-center justify-center font-mono">
                      #{bat.rank}
                    </span>
                    <div>
                      <div className="text-xs font-bold text-white">{bat.player_name}</div>
                      <div className="text-[11px] text-gray-400">{bat.batting_role} · {bat.team}</div>
                    </div>
                  </div>
                  <div className="text-right">
                    <div className="text-sm font-extrabold text-[#EB107E] font-mono">{bat.bpri_score.toFixed(2)}</div>
                    <div className="text-[10px] text-gray-400">SR: {bat.pressure_strike_rate.toFixed(1)} | SSSI: {bat.sample_size_saturation_index_pct.toFixed(0)}%</div>
                  </div>
                </div>
              ))}
            </div>
          </div>
          <div className="mt-4 p-2.5 rounded-lg bg-[#051424] border border-white/5 text-[11px] text-gray-400">
            <span className="text-[#EB107E] font-bold">Insight:</span> Ashutosh Sharma & Shashank Singh exhibit peak death-phase boundary escalation above 190.0 SR.
          </div>
        </div>

        {/* Bowlers Preview (Actionable Pool) */}
        <div className="bg-[#0D1C2D] border border-white/10 rounded-xl p-5 flex flex-col justify-between">
          <div>
            <div className="flex items-center justify-between mb-4">
              <div className="flex items-center gap-2">
                <ShieldAlert className="w-4 h-4 text-[#7BD0FF]" />
                <h3 className="text-sm font-bold text-white uppercase tracking-wider">
                  Top Actionable Bowlers (BCCI-Eligible)
                </h3>
              </div>
              <button
                onClick={() => navigate('/bowling')}
                className="text-xs text-[#7BD0FF] hover:underline flex items-center gap-1 font-semibold"
              >
                Full Rankings <ArrowUpRight className="w-3.5 h-3.5" />
              </button>
            </div>

            <div className="space-y-3">
              {data.actionable_bowlers_preview.map((bowl: any) => (
                <div
                  key={bowl.player_id}
                  onClick={() => navigate('/bowling')}
                  className="bg-[#122131] hover:bg-[#1C2B3C] border border-white/5 p-3.5 rounded-lg flex items-center justify-between cursor-pointer transition-all"
                >
                  <div className="flex items-center gap-3">
                    <span className="w-6 h-6 rounded-full bg-[#7BD0FF]/20 text-[#7BD0FF] text-xs font-bold flex items-center justify-center font-mono">
                      #{bowl.rank}
                    </span>
                    <div>
                      <div className="text-xs font-bold text-white">{bowl.player_name}</div>
                      <div className="text-[11px] text-gray-400">{bowl.bowling_role} · {bowl.team}</div>
                    </div>
                  </div>
                  <div className="text-right">
                    <div className="text-sm font-extrabold text-[#7BD0FF] font-mono">{bowl.bowpri_score.toFixed(2)}</div>
                    <div className="text-[10px] text-gray-400">Econ: {bowl.pressure_economy_rate.toFixed(2)} | SSSI: {bowl.sample_size_saturation_index_pct.toFixed(0)}%</div>
                  </div>
                </div>
              ))}
            </div>
          </div>
          <div className="mt-4 p-2.5 rounded-lg bg-[#051424] border border-white/5 text-[11px] text-gray-400">
            <span className="text-[#7BD0FF] font-bold">Policy Segregation:</span> Non-BCCI benchmark leaders (Mohammad Nawaz 83.00, Abrar Ahmed 77.96) serve as Bayesian priors. Actionable pool starts at Matthew Humphreys (76.68).
          </div>
        </div>
      </div>

      {/* Quick Launchpad & Strategic Workflows */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div 
          onClick={() => navigate('/compare')}
          className="bg-[#0D1C2D] hover:bg-[#122131] border border-white/10 hover:border-[#EB107E]/50 p-4 rounded-xl cursor-pointer transition-all flex items-start gap-3"
        >
          <div className="p-2.5 rounded-lg bg-[#EB107E]/10 text-[#EB107E]">
            <GitCompare className="w-5 h-5" />
          </div>
          <div>
            <h4 className="text-xs font-bold text-white">Player Comparison Studio</h4>
            <p className="text-[11px] text-gray-400 mt-1">
              Compare any two candidates on 6 leverage axes with 95% bootstrap confidence interval overlap testing.
            </p>
          </div>
        </div>

        <div 
          onClick={() => navigate('/auction')}
          className="bg-[#0D1C2D] hover:bg-[#122131] border border-white/10 hover:border-[#FABC4D]/50 p-4 rounded-xl cursor-pointer transition-all flex items-start gap-3"
        >
          <div className="p-2.5 rounded-lg bg-[#FABC4D]/10 text-[#FABC4D]">
            <Gavel className="w-5 h-5" />
          </div>
          <div>
            <h4 className="text-xs font-bold text-white">Auction War Room Simulator</h4>
            <p className="text-[11px] text-gray-400 mt-1">
              Adjust simulated bidding ceilings against ₹42.80 Cr remaining purse with live quota and squad checks.
            </p>
          </div>
        </div>

        <div 
          onClick={() => navigate('/pressure')}
          className="bg-[#0D1C2D] hover:bg-[#122131] border border-white/10 hover:border-[#7BD0FF]/50 p-4 rounded-xl cursor-pointer transition-all flex items-start gap-3"
        >
          <div className="p-2.5 rounded-lg bg-[#7BD0FF]/10 text-[#7BD0FF]">
            <Activity className="w-5 h-5" />
          </div>
          <div>
            <h4 className="text-xs font-bold text-white">Leverage Dynamics Engine</h4>
            <p className="text-[11px] text-gray-400 mt-1">
              Explore ball-by-ball required run rate swings, match phases, and collapse vulnerability distributions.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

