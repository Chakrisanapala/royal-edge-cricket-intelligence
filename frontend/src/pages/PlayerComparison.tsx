import React, { useEffect, useState } from 'react';
import { api, CompareResult, Batter, Bowler } from '../services/api';
import { 
  ResponsiveContainer, 
  RadarChart, 
  PolarGrid, 
  PolarAngleAxis, 
  PolarRadiusAxis, 
  Radar, 
  Legend, 
  Tooltip 
} from 'recharts';
import { GitCompare, AlertTriangle, CheckCircle2, Info, ArrowRight } from 'lucide-react';

export const PlayerComparison: React.FC = () => {
  const [playerType, setPlayerType] = useState<'batter' | 'bowler'>('batter');
  const [battersList, setBattersList] = useState<Batter[]>([]);
  const [bowlersList, setBowlersList] = useState<Bowler[]>([]);
  
  const [playerAId, setPlayerAId] = useState<number>(8101); // Ashutosh Sharma
  const [playerBId, setPlayerBId] = useState<number>(2756); // Shashank Singh

  const [compareData, setCompareData] = useState<CompareResult | null>(null);
  const [loading, setLoading] = useState(true);

  // Initial load of player options
  useEffect(() => {
    Promise.all([
      api.getBatters(),
      api.getBowlers()
    ]).then(([bats, bowls]) => {
      setBattersList(bats);
      setBowlersList(bowls);
      if (playerType === 'batter' && bats.length >= 2) {
        setPlayerAId(bats[0].player_id);
        setPlayerBId(bats[1].player_id);
      } else if (playerType === 'bowler' && bowls.length >= 2) {
        setPlayerAId(bowls[0].player_id);
        setPlayerBId(bowls[1].player_id);
      }
    });
  }, [playerType]);

  // Execute comparison when players change
  useEffect(() => {
    if (playerAId && playerBId) {
      setLoading(true);
      api.comparePlayers(playerAId, playerBId, playerType)
        .then(res => {
          setCompareData(res);
          setLoading(false);
        })
        .catch(err => {
          console.error(err);
          setLoading(false);
        });
    }
  }, [playerAId, playerBId, playerType]);

  const handleTypeSwitch = (type: 'batter' | 'bowler') => {
    setPlayerType(type);
    if (type === 'batter' && battersList.length >= 2) {
      setPlayerAId(battersList[0].player_id);
      setPlayerBId(battersList[1].player_id);
    } else if (type === 'bowler' && bowlersList.length >= 2) {
      setPlayerAId(bowlersList[0].player_id);
      setPlayerBId(bowlersList[1].player_id);
    }
  };

  const currentList = playerType === 'batter' ? battersList : bowlersList;

  return (
    <div className="space-y-6">
      {/* Header & Controls */}
      <div className="bg-[#0D1C2D] border border-white/10 rounded-xl p-5 flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <div className="flex items-center gap-2">
            <span className="px-2.5 py-0.5 rounded bg-[#EB107E]/20 text-[#EB107E] text-[10px] font-bold uppercase">
              Head-to-Head Analytics
            </span>
            <span className="text-xs text-gray-400">Statistical Significance Studio</span>
          </div>
          <h2 className="text-xl font-bold text-white mt-1">Player Comparison & Uncertainty Overlap</h2>
          <p className="text-xs text-gray-400 mt-0.5">
            Evaluating multi-dimensional pressure capabilities alongside 95% bootstrap confidence intervals.
          </p>
        </div>

        {/* Player Type Switch */}
        <div className="flex items-center bg-[#122131] border border-white/10 rounded-lg p-1">
          <button
            onClick={() => handleTypeSwitch('batter')}
            className={`px-4 py-1.5 rounded-md text-xs font-bold transition-all ${
              playerType === 'batter'
                ? 'bg-[#EB107E] text-white shadow-sm'
                : 'text-gray-400 hover:text-white'
            }`}
          >
            Batters Comparison
          </button>
          <button
            onClick={() => handleTypeSwitch('bowler')}
            className={`px-4 py-1.5 rounded-md text-xs font-bold transition-all ${
              playerType === 'bowler'
                ? 'bg-[#7BD0FF] text-[#051424] shadow-sm font-extrabold'
                : 'text-gray-400 hover:text-white'
            }`}
          >
            Bowlers Comparison
          </button>
        </div>
      </div>

      {/* Selectors Bar */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {/* Player A Selector */}
        <div className="bg-[#0D1C2D] border border-[#EB107E]/30 rounded-xl p-4">
          <label className="text-xs font-bold text-[#EB107E] block mb-2 uppercase tracking-wider">
            Player A (Benchmark Candidate)
          </label>
          <select
            value={playerAId}
            onChange={(e) => setPlayerAId(Number(e.target.value))}
            className="w-full bg-[#122131] border border-white/10 rounded-lg px-3 py-2 text-xs text-white focus:outline-none focus:border-[#EB107E]"
          >
            {currentList.map(p => (
              <option key={p.player_id} value={p.player_id}>
                {p.player_name} ({p.team}) — Score: {(playerType === 'batter' ? (p as Batter).bpri_score : (p as Bowler).bowpri_score).toFixed(2)}
              </option>
            ))}
          </select>
        </div>

        {/* Player B Selector */}
        <div className="bg-[#0D1C2D] border border-[#7BD0FF]/30 rounded-xl p-4">
          <label className="text-xs font-bold text-[#7BD0FF] block mb-2 uppercase tracking-wider">
            Player B (Alternative Candidate)
          </label>
          <select
            value={playerBId}
            onChange={(e) => setPlayerBId(Number(e.target.value))}
            className="w-full bg-[#122131] border border-white/10 rounded-lg px-3 py-2 text-xs text-white focus:outline-none focus:border-[#7BD0FF]"
          >
            {currentList.map(p => (
              <option key={p.player_id} value={p.player_id}>
                {p.player_name} ({p.team}) — Score: {(playerType === 'batter' ? (p as Batter).bpri_score : (p as Bowler).bowpri_score).toFixed(2)}
              </option>
            ))}
          </select>
        </div>
      </div>

      {loading || !compareData ? (
        <div className="flex items-center justify-center h-80 bg-[#0D1C2D] border border-white/10 rounded-xl">
          <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-[#EB107E]"></div>
        </div>
      ) : (
        <>
          {/* Statistical Uncertainty Status Banner */}
          <div className={`p-4 rounded-xl border flex items-start gap-3 ${
            compareData.ci_overlap 
              ? 'bg-[#FABC4D]/10 border-[#FABC4D]/30 text-[#FABC4D]' 
              : 'bg-emerald-950/30 border-emerald-500/30 text-emerald-300'
          }`}>
            {compareData.ci_overlap ? (
              <AlertTriangle className="w-5 h-5 shrink-0 mt-0.5 text-[#FABC4D]" />
            ) : (
              <CheckCircle2 className="w-5 h-5 shrink-0 mt-0.5 text-emerald-400" />
            )}
            <div>
              <div className="text-xs font-bold uppercase tracking-wider">
                {compareData.ci_overlap ? 'Confidence Interval Overlap Detected' : 'Statistically Distinct Performance'}
              </div>
              <p className="text-xs mt-1 text-gray-300 leading-relaxed">
                {compareData.uncertainty_note}
              </p>
            </div>
          </div>

          {/* Radar Chart & Metric Comparison Grid */}
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
            {/* 6-Axis Radar Chart */}
            <div className="lg:col-span-7 bg-[#0D1C2D] border border-white/10 rounded-xl p-5 flex flex-col justify-between">
              <div className="flex items-center justify-between mb-2">
                <h3 className="text-sm font-bold text-white uppercase tracking-wider">
                  6-Dimensional Leverage Radar
                </h3>
                <span className="text-[11px] text-gray-400 font-mono">0–100 Normalized Scale</span>
              </div>

              <div className="h-80 w-full">
                <ResponsiveContainer width="100%" height="100%">
                  <RadarChart cx="50%" cy="50%" outerRadius="80%" data={compareData.radar_data}>
                    <PolarGrid stroke="#273647" />
                    <PolarAngleAxis dataKey="metric" stroke="#94A3B8" fontSize={11} />
                    <PolarRadiusAxis angle={30} domain={[0, 100]} stroke="#334155" fontSize={10} />
                    <Radar
                      name={compareData.player_a.name}
                      dataKey="player_a"
                      stroke="#EB107E"
                      fill="#EB107E"
                      fillOpacity={0.4}
                    />
                    <Radar
                      name={compareData.player_b.name}
                      dataKey="player_b"
                      stroke="#7BD0FF"
                      fill="#7BD0FF"
                      fillOpacity={0.3}
                    />
                    <Legend wrapperStyle={{ fontSize: '12px', paddingTop: '10px' }} />
                    <Tooltip 
                      contentStyle={{ backgroundColor: '#0D1C2D', borderColor: '#334155', borderRadius: '8px', fontSize: '11px' }}
                    />
                  </RadarChart>
                </ResponsiveContainer>
              </div>

              <div className="text-[11px] text-gray-400 text-center mt-2 border-t border-white/5 pt-2">
                Scores reflect Bayesian-shrunk reliability components across powerplay, middle leverage, and death overs.
              </div>
            </div>

            {/* Direct Delta & Sample Comparison */}
            <div className="lg:col-span-5 bg-[#0D1C2D] border border-white/10 rounded-xl p-5 flex flex-col justify-between">
              <div>
                <h3 className="text-sm font-bold text-white uppercase tracking-wider mb-4">
                  Head-to-Head Metric Deltas
                </h3>

                <div className="space-y-3">
                  {/* Total Score Delta */}
                  <div className="bg-[#122131] border border-white/5 rounded-lg p-3.5 flex items-center justify-between">
                    <div>
                      <span className="text-[11px] text-gray-400 block">Overall Composite Score</span>
                      <span className="text-xs font-bold text-white">
                        {compareData.player_a.name} vs {compareData.player_b.name}
                      </span>
                    </div>
                    <div className="text-right">
                      <span className="text-sm font-mono font-extrabold text-[#EB107E]">
                        {compareData.deltas.score_delta > 0 ? '+' : ''}{compareData.deltas.score_delta.toFixed(2)}
                      </span>
                      <span className="text-[10px] text-gray-400 block font-mono">
                        {compareData.player_a.score.toFixed(2)} vs {compareData.player_b.score.toFixed(2)}
                      </span>
                    </div>
                  </div>

                  {/* 95% Confidence Intervals */}
                  <div className="bg-[#122131] border border-white/5 rounded-lg p-3.5 space-y-2">
                    <span className="text-[11px] text-gray-400 block font-semibold">95% Bootstrap Intervals</span>
                    <div className="flex items-center justify-between text-xs">
                      <span className="text-[#EB107E] font-semibold">{compareData.player_a.name}</span>
                      <span className="font-mono text-white">
                        [{compareData.player_a.ci[0].toFixed(1)}, {compareData.player_a.ci[1].toFixed(1)}]
                      </span>
                    </div>
                    <div className="flex items-center justify-between text-xs">
                      <span className="text-[#7BD0FF] font-semibold">{compareData.player_b.name}</span>
                      <span className="font-mono text-white">
                        [{compareData.player_b.ci[0].toFixed(1)}, {compareData.player_b.ci[1].toFixed(1)}]
                      </span>
                    </div>
                  </div>

                  {/* SSSI Saturation */}
                  <div className="bg-[#122131] border border-white/5 rounded-lg p-3.5 space-y-2">
                    <div className="flex items-center justify-between">
                      <span className="text-[11px] text-gray-400 font-semibold">Sample Size Saturation (SSSI)</span>
                      <span className="text-[10px] font-mono text-gray-300">
                        Diff: {compareData.deltas.sssi_diff > 0 ? '+' : ''}{compareData.deltas.sssi_diff.toFixed(1)}%
                      </span>
                    </div>
                    <div className="flex items-center justify-between text-xs">
                      <span className="text-white">{compareData.player_a.name}</span>
                      <span className="font-mono font-bold text-[#EB107E]">{compareData.player_a.sssi.toFixed(1)}%</span>
                    </div>
                    <div className="flex items-center justify-between text-xs">
                      <span className="text-white">{compareData.player_b.name}</span>
                      <span className="font-mono font-bold text-[#7BD0FF]">{compareData.player_b.sssi.toFixed(1)}%</span>
                    </div>
                  </div>
                </div>
              </div>

              <div className="mt-4 p-2.5 rounded-lg bg-[#051424] border border-white/5 text-[11px] text-gray-400">
                <span className="text-[#FABC4D] font-bold">Cautionary Guidance: </span>
                If SSSI differs by &gt;20%, avoid evaluating scores as direct talent equivalents; smaller sample sizes suffer wider shrinkage adjustment.
              </div>
            </div>
          </div>
        </>
      )}
    </div>
  );
};

