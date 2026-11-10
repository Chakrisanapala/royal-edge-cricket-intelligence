import React, { useState, useEffect } from 'react';
import { useSearchParams } from 'react-router-dom';
import { api, Batter, Bowler } from '../services/api';
import { 
  UserCheck, 
  Target, 
  ShieldAlert, 
  Activity, 
  Award, 
  CheckCircle2, 
  AlertCircle, 
  BarChart3, 
  Clock 
} from 'lucide-react';

export const PlayerProfiles: React.FC = () => {
  const [searchParams, setSearchParams] = useSearchParams();
  const initialId = searchParams.get('id') ? Number(searchParams.get('id')) : 8101; // Ashutosh Sharma default

  const [selectedId, setSelectedId] = useState<number>(initialId);
  const [profile, setProfile] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  const [allPlayers, setAllPlayers] = useState<Array<{ id: number; name: string; type: string }>>([]);

  useEffect(() => {
    Promise.all([api.getBatters(), api.getBowlers()]).then(([bats, bowls]) => {
      const combined = [
        ...bats.map(b => ({ id: b.player_id, name: `${b.player_name} (Batter)`, type: 'batter' })),
        ...bowls.map(b => ({ id: b.player_id, name: `${b.player_name} (Bowler)`, type: 'bowler' }))
      ];
      setAllPlayers(combined);
    });
  }, []);

  useEffect(() => {
    if (selectedId) {
      setLoading(true);
      api.getPlayerProfile(selectedId)
        .then(res => {
          setProfile(res);
          setLoading(false);
        })
        .catch(err => {
          console.error(err);
          setLoading(false);
        });
    }
  }, [selectedId]);

  const handleSelect = (id: number) => {
    setSelectedId(id);
    setSearchParams({ id: String(id) });
  };

  return (
    <div className="space-y-6">
      {/* Top Selector Bar */}
      <div className="bg-[#0D1C2D] border border-white/10 rounded-xl p-4 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <span className="text-[10px] text-[#EB107E] font-bold uppercase tracking-wider block">
            Front-Office Dossier
          </span>
          <h2 className="text-lg font-bold text-white">Player Intelligence Profile</h2>
        </div>

        <div className="w-72">
          <select
            value={selectedId}
            onChange={(e) => handleSelect(Number(e.target.value))}
            className="w-full bg-[#122131] border border-white/10 rounded-lg px-3 py-2 text-xs text-white focus:outline-none focus:border-[#EB107E]"
          >
            {allPlayers.map(p => (
              <option key={p.id} value={p.id}>{p.name}</option>
            ))}
          </select>
        </div>
      </div>

      {loading || !profile ? (
        <div className="flex items-center justify-center h-80 bg-[#0D1C2D] border border-white/10 rounded-xl">
          <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-[#EB107E]"></div>
        </div>
      ) : (
        <div className="space-y-6">
          {/* Identity Header Card */}
          <div className="bg-[#0D1C2D] border border-white/10 rounded-xl p-6 relative overflow-hidden">
            <div className="absolute top-0 right-0 w-64 h-64 bg-[#EB107E]/10 rounded-full blur-3xl pointer-events-none"></div>
            <div className="flex flex-col md:flex-row md:items-center justify-between gap-6 relative z-10">
              <div className="flex items-center gap-4">
                <div className="w-16 h-16 rounded-2xl bg-gradient-to-br from-[#1C2B3C] to-[#122131] border border-white/15 flex items-center justify-center text-2xl font-bold font-mono text-white shadow-lg">
                  {profile.identity.player_name.charAt(0)}
                </div>
                <div>
                  <div className="flex items-center gap-2">
                    <h3 className="text-2xl font-extrabold text-white">{profile.identity.player_name}</h3>
                    <span className="px-2.5 py-0.5 rounded bg-[#EB107E]/20 text-[#EB107E] text-xs font-mono font-bold">
                      Rank #{profile.core_metrics.rank}
                    </span>
                  </div>
                  <div className="text-xs text-gray-300 mt-1">
                    {profile.identity.role} · <span className="text-white font-medium">{profile.identity.team}</span>
                  </div>
                  <div className="mt-2">
                    <span className="text-[10px] px-2 py-0.5 rounded bg-white/5 border border-white/10 text-emerald-400 font-semibold">
                      {profile.identity.eligibility}
                    </span>
                  </div>
                </div>
              </div>

              {/* Score Display */}
              <div className="flex items-center gap-6 border-t md:border-t-0 md:border-l border-white/10 pt-4 md:pt-0 md:pl-6">
                <div>
                  <div className="text-xs text-gray-400 uppercase font-semibold">{profile.core_metrics.score_label}</div>
                  <div className="text-4xl font-extrabold text-[#EB107E] font-mono mt-1">
                    {profile.core_metrics.score.toFixed(2)}
                  </div>
                </div>
                <div>
                  <div className="text-xs text-gray-400 uppercase font-semibold">Sample SSSI</div>
                  <div className="text-4xl font-extrabold text-[#FABC4D] font-mono mt-1">
                    {profile.uncertainty.sssi_pct.toFixed(0)}%
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Metric Details Grid */}
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
            {profile.player_type === 'batter' ? (
              <>
                <div className="bg-[#0D1C2D] border border-white/10 rounded-xl p-4">
                  <span className="text-xs text-gray-400 block">High-Pressure Strike Rate</span>
                  <div className="text-2xl font-bold font-mono text-white mt-1">
                    {profile.core_metrics.hp_strike_rate.toFixed(1)}
                  </div>
                  <span className="text-[11px] text-emerald-400 mt-1 block">
                    +{profile.core_metrics.delta_vs_normal.toFixed(1)} vs normal play
                  </span>
                </div>
                <div className="bg-[#0D1C2D] border border-white/10 rounded-xl p-4">
                  <span className="text-xs text-gray-400 block">Death Overs SR (16–20)</span>
                  <div className="text-2xl font-bold font-mono text-[#FABC4D] mt-1">
                    {profile.core_metrics.death_strike_rate.toFixed(1)}
                  </div>
                  <span className="text-[11px] text-gray-400 mt-1 block">Leverage escalation</span>
                </div>
                <div className="bg-[#0D1C2D] border border-white/10 rounded-xl p-4">
                  <span className="text-xs text-gray-400 block">Chase Strike Rate</span>
                  <div className="text-2xl font-bold font-mono text-white mt-1">
                    {profile.core_metrics.chase_strike_rate.toFixed(1)}
                  </div>
                  <span className="text-[11px] text-gray-400 mt-1 block">2nd Innings pacing</span>
                </div>
                <div className="bg-[#0D1C2D] border border-white/10 rounded-xl p-4">
                  <span className="text-xs text-gray-400 block">Pressure Balls Faced</span>
                  <div className="text-2xl font-bold font-mono text-[#7BD0FF] mt-1">
                    {profile.core_metrics.pressure_balls_faced}
                  </div>
                  <span className="text-[11px] text-gray-400 mt-1 block">Across {profile.core_metrics.matches_analyzed} matches</span>
                </div>
              </>
            ) : (
              <>
                <div className="bg-[#0D1C2D] border border-white/10 rounded-xl p-4">
                  <span className="text-xs text-gray-400 block">High-Pressure Economy</span>
                  <div className="text-2xl font-bold font-mono text-white mt-1">
                    {profile.core_metrics.hp_economy_rate.toFixed(2)}
                  </div>
                  <span className="text-[11px] text-emerald-400 mt-1 block">
                    {profile.core_metrics.delta_vs_normal >= 0 ? '+' : ''}{profile.core_metrics.delta_vs_normal.toFixed(2)} vs normal
                  </span>
                </div>
                <div className="bg-[#0D1C2D] border border-white/10 rounded-xl p-4">
                  <span className="text-xs text-gray-400 block">Death Economy (16–20)</span>
                  <div className="text-2xl font-bold font-mono text-[#FABC4D] mt-1">
                    {profile.core_metrics.death_economy_rate.toFixed(2)}
                  </div>
                  <span className="text-[11px] text-gray-400 mt-1 block">Critical overs containment</span>
                </div>
                <div className="bg-[#0D1C2D] border border-white/10 rounded-xl p-4">
                  <span className="text-xs text-gray-400 block">Pressure Wickets Taken</span>
                  <div className="text-2xl font-bold font-mono text-[#7BD0FF] mt-1">
                    {profile.core_metrics.pressure_wickets}
                  </div>
                  <span className="text-[11px] text-gray-400 mt-1 block">Avg: {profile.core_metrics.hp_bowling_avg.toFixed(1)}</span>
                </div>
                <div className="bg-[#0D1C2D] border border-white/10 rounded-xl p-4">
                  <span className="text-xs text-gray-400 block">Pressure Legal Balls</span>
                  <div className="text-2xl font-bold font-mono text-white mt-1">
                    {profile.core_metrics.pressure_legal_balls}
                  </div>
                  <span className="text-[11px] text-gray-400 mt-1 block">{profile.core_metrics.pressure_overs_bowled} total overs</span>
                </div>
              </>
            )}
          </div>

          {/* Uncertainty & Statistical Bounds */}
          <div className="bg-[#0D1C2D] border border-white/10 rounded-xl p-5">
            <h4 className="text-xs font-bold text-[#FABC4D] uppercase tracking-wider mb-2">
              Statistical Reliability & Uncertainty Bounds
            </h4>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
              <div className="bg-[#122131] p-3.5 rounded-lg border border-white/5">
                <span className="text-[11px] text-gray-400 block">Bootstrap 95% Confidence Interval</span>
                <span className="text-sm font-mono font-bold text-white block mt-1">
                  [{profile.uncertainty.ci_lower.toFixed(2)}, {profile.uncertainty.ci_upper.toFixed(2)}]
                </span>
                <span className="text-[10px] text-gray-400 block mt-1">
                  Standard Error: ±{profile.uncertainty.standard_error.toFixed(2)}
                </span>
              </div>

              <div className="bg-[#122131] p-3.5 rounded-lg border border-white/5 md:col-span-2">
                <span className="text-[11px] text-gray-400 block">Scientific Interpretation</span>
                <p className="text-xs text-gray-300 mt-1 leading-relaxed">
                  {profile.uncertainty.interpretation}
                </p>
              </div>
            </div>
          </div>

          {/* Phase-by-Phase Breakdown & Evidence-Based Observations */}
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
            {/* Phase Breakdown */}
            <div className="bg-[#0D1C2D] border border-white/10 rounded-xl p-5">
              <h4 className="text-xs font-bold text-white uppercase tracking-wider mb-3">
                Phase-by-Phase Pressure Breakdown
              </h4>
              <div className="space-y-3">
                {profile.phase_breakdown.map((p: any) => (
                  <div key={p.phase} className="bg-[#122131] p-3 rounded-lg border border-white/5 flex items-center justify-between text-xs">
                    <div>
                      <span className="font-bold text-white block">{p.phase}</span>
                      <span className="text-[11px] text-gray-400">
                        {profile.player_type === 'batter' ? `${p.balls} balls faced · ${p.runs} runs` : `${p.overs} overs · ${p.wickets} wkts`}
                      </span>
                    </div>
                    <div className="text-right font-mono">
                      <span className="text-sm font-bold text-[#EB107E]">
                        {profile.player_type === 'batter' ? `${p.strike_rate.toFixed(1)} SR` : `${p.economy.toFixed(2)} Econ`}
                      </span>
                    </div>
                  </div>
                ))}
              </div>
            </div>

            {/* Evidence-Based Scouting Observations */}
            <div className="bg-[#0D1C2D] border border-white/10 rounded-xl p-5 flex flex-col justify-between">
              <div>
                <h4 className="text-xs font-bold text-white uppercase tracking-wider mb-3">
                  Evidence-Based Scouting Insights
                </h4>
                <div className="space-y-2.5">
                  {profile.scouting_observations.map((obs: string, idx: number) => (
                    <div key={idx} className="flex items-start gap-2 text-xs text-gray-300 bg-[#122131] p-3 rounded-lg border border-white/5">
                      <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0 mt-0.5" />
                      <span>{obs}</span>
                    </div>
                  ))}
                </div>
              </div>
              <div className="mt-4 text-[10px] text-gray-500 italic">
                * Note: Observations derive entirely from verified ball-by-ball delivery records (2022–2026).
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

